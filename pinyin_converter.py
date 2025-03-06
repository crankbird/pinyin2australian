# Copyright (c) 2025 RIchard John Martin aka crankbird
# Portions of this code were generated with the help of OpenAI's ChatGPT.
# This file is part of the New English Approximation Pinyin Converter project.
#
# Licensed under the MIT License. You may obtain a copy of the License at
# https://opensource.org/licenses/MIT


import pandas as pd
import re
import unicodedata

def normalize_text(text):
    """Normalize text to NFC form to ensure accented characters are standard."""
    return unicodedata.normalize('NFC', text)

def segment_and_capitalize(text):
    """Segment text into syllables based on tone-marked vowels and capitalize the final syllable's first letter."""
    tone_chars = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"
    pattern = r"([a-zA-Z']*[{}][a-zA-Z]*)".format(tone_chars)
    syllables = re.findall(pattern, text)
    if not syllables:
        return text
    last_index = 0
    segments = []
    for syll in syllables:
        idx = text.find(syll, last_index)
        if idx != -1:
            segments.append(syll)
            last_index = idx + len(syll)
    if last_index < len(text):
        segments[-1] = segments[-1] + text[last_index:]
    if len(segments) > 1:
        segments[-1] = segments[-1].capitalize()
    return "-".join(segments)

def convert_pinyin(text):
    """Convert standard Mandarin Pinyin to the New English Approximation format."""
    if not isinstance(text, str):
        return text
    text = normalize_text(text)
    
    # Rule 2: Special case for "shi"
    def replace_shi(match):
        tone = match.group(1) if match.group(1) else 'ì'
        return f"shrr({tone})"
    text = re.sub(r'shi([ìíǐ]?)\b', replace_shi, text, flags=re.UNICODE)
    
    # Rule 1: Retroflex Consonants
    text = re.sub(r'zh', 'zhrr', text, flags=re.UNICODE)
    text = re.sub(r'ch', 'chrr', text, flags=re.UNICODE)
    text = re.sub(r'sh', 'shrr', text, flags=re.UNICODE)
    text = re.sub(r'\br', 'rr', text, flags=re.UNICODE)
    
    # Rule 5: Consonant Aspiration
    text = re.sub(r'\bp', "p'", text, flags=re.UNICODE)
    text = re.sub(r'\bt', "t'", text, flags=re.UNICODE)
    text = re.sub(r'\bk', "k'", text, flags=re.UNICODE)
    text = re.sub(r'\bc', "ts'", text, flags=re.UNICODE)
    
    # Rule 6: Standardisation for “q”
    text = re.sub(r'q', "tsyh'", text, flags=re.UNICODE)
    
    # Rule 7: Other Initial Consonant Mappings
    text = re.sub(r'x', 'ssy', text, flags=re.UNICODE)
    text = re.sub(r'j', 'jy', text, flags=re.UNICODE)
    text = re.sub(r'z', 'dz', text, flags=re.UNICODE)
    
    # Rule 8: Vowel and Diphthong Adjustments
    text = re.sub(r'ao', 'ahw', text, flags=re.UNICODE)
    text = re.sub(r'ai', 'ahì', text, flags=re.UNICODE)
    text = re.sub(r'ei', 'ey', text, flags=re.UNICODE)
    text = re.sub(r'ou', 'ow', text, flags=re.UNICODE)
    
    # Rule 3: Open Vowel "a" Adjustment:
    # Append an "h" to any "a" with a tone diacritic (ā, á, ǎ, à) if not already followed by "h"
    text = re.sub(r'([aàáǎā])(?!h)', r'\1h', text, flags=re.UNICODE)
    
    # Rule 9: Unvoiced Vowels After z, c, s
    text = re.sub(r'(dz)([iìíǐ])', r"\1(\2)", text, flags=re.UNICODE)
    text = re.sub(r"(ts')([iìíǐ])", r"\1(\2)", text, flags=re.UNICODE)
    text = re.sub(r'(s)([iìíǐ])', r"\1(\2)", text, flags=re.UNICODE)
    
    # Rule 12: “er” (儿化音) conversion
    text = re.sub(r'er\b', 'arr', text, flags=re.UNICODE)
    
    # Updated Rule 10: Neutral Tone Handling
    # For syllables like "de", "le", "re", preserve the initial consonant:
    text = re.sub(r'\b([bpmfdtnlgkhjqxrzcsyw])e\b', r'\1uh', text, flags=re.UNICODE)
    # For standalone "e", convert to "uh"
    text = re.sub(r'\be\b', 'uh', text, flags=re.UNICODE)
    
    # Rule 4: Syllable Segmentation & Capitalisation
    text = segment_and_capitalize(text)
    
    return text

def process_csv(input_path, output_path):
    # Read the CSV file (ensure it has a 'Pinyin' column)
    df = pd.read_csv(input_path)
    if 'Pinyin' in df.columns:
        df['australian approximation'] = df['Pinyin'].apply(convert_pinyin)
    else:
        raise ValueError("No 'Pinyin' column found in the CSV.")
    
    # Save the updated CSV
    df.to_csv(output_path, index=False)
    print("File saved to", output_path)

# Example usage:
if __name__ == "__main__":
    input_csv = "pinyin.csv"  # Adjust if needed
    output_csv = "pinyin-converted.csv"  # The output file name
    process_csv(input_csv, output_csv)
