# pinyin2australian English Approximation Pinyin Converter
My attempt at turning pinyin into something that I can read directily on an autocue and not be horribly wrong

## Overview

This project implements a converter that transforms standard Mandarin Pinyin into a New Australian English Approximation format. The converter applies a comprehensive set of conversion rules to provide a phonetic transcription that aims to be intuitive for learners of Mandarin.

## Features

- **Retroflex Consonant Handling:**  
  - Converts "zh" to **zhrr**, "ch" to **chrr**, "sh" to **shrr**, and initial "r" to **rr...** (e.g., "rén" → **rrzén**).

- **Special Case for “shi”:**  
  - Transforms any form of "shi" (shì, shí, shǐ, or shi) into **shrr(…)** with the tone indicated in parentheses (e.g., shì → **shrr(ì)**).

- **Open Vowel "a" Adjustment:**  
  - Appends an "h" to any occurrence of "a" with a tone diacritic (e.g., "guān" → **guāhn**, "xiǎng" → **xiǎhng**) to indicate the open, resonant sound.

- **Syllable Segmentation & Capitalisation:**  
  - Hyphenates multi‑syllable words for clarity, with the first letter of the final syllable capitalised (e.g., huànjùhuàshuō → **huàhn-jù-huà-Shuō**).

- **Consonant Aspiration:**  
  - Marks aspirated consonants with an apostrophe (e.g., p → **p’**, t → **t’**, k → **k’**, c → **ts’**).

- **Standardisation for “q”:**  
  - Replaces "q" with **tsyh’** (e.g., qù → **tsyh’ù**).

- **Other Consonant Mappings:**  
  - Maps "x" to **ssy**, "j" to **jy**, and "z" (unaspirated "ts") to **dz**.

- **Vowel and Diphthong Adjustments:**  
  - Adjusts diphthongs:  
    - "ao" → **ahw** (as in “cow” (kind of))  
    - "ai" → **ahì** (similar to “eye”)  
    - "ei" → **ey**  
    - "ou" → **ow**  
  - A standalone "e" becomes **uh**.

- **Unvoiced Vowels:**  
  - Encloses the vowel in syllables like "zi", "ci", and "si" in parentheses (e.g., zi → **dz(ì)**).

- **Neutral Tone Handling:**  
  - For syllables with a neutral tone that start with a consonant (e.g., "de", "le", "re"), the initial consonant is preserved and the vowel is reduced (e.g., de → **duh**, le → **luh**, re → **ruh**).  
  - A standalone "e" is converted to **uh**.

- **Umlaut “ü”:**  
  - The character “ü” is preserved as is.

- **“er” (儿化音) Conversion:**  
  - Converts the "er" sound to **arr**.

## Usage

1. **Setup:**  
   Ensure you have Python 3 installed. Clone or download this repository and place your input CSV file (which should have a column named `Pinyin`) in the project directory.

2. **Running the Converter:**  
   Run the script by executing:
   ```bash
   python pinyin_converter.py

   By default, the script writes its output to a file named pinyin-converted.csv. If you'd like to use a different file name or location, you can change this by modifying the output_csv (or output_path) variable in the script.
