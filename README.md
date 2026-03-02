# Hard Vocabulary Reader for Exam Preparation

English vocabulary learning tool specialized for difficult words commonly found in standardized exams (SAT, GRE, TOEFL, etc.)

## 📚 Features

- **Study Mode**: Browse and learn all vocabulary words with definitions, examples, and synonyms
- **Quiz Mode**: Test your knowledge interactively
- **Difficulty Levels**: Filter words by difficulty (Intermediate, Advanced, Expert)
- **Word Search**: Look up specific words quickly
- **Statistics**: Track your vocabulary learning progress

## 🚀 Usage

### Running the Interactive Reader

```bash
python3 vocab_reader.py
```

### Menu Options

1. **Study Mode** - Browse all words with complete information
2. **Quiz Mode** - Interactive self-testing
3. **Filter by Difficulty** - Focus on specific difficulty levels
4. **Search for a word** - Find specific vocabulary words
5. **Show Statistics** - View vocabulary distribution
6. **Exit** - Close the program

## 📖 Vocabulary Database

The vocabulary list includes 15 carefully selected difficult English words, each with:
- Pronunciation guide (IPA)
- Part of speech
- Clear definition
- Example sentence
- Synonyms
- Difficulty level

### Sample Words Included

- **Ephemeral** - Lasting for a very short time
- **Ubiquitous** - Present everywhere
- **Perspicacious** - Having keen insight
- **Obfuscate** - To make unclear or confusing
- **Magnanimous** - Generous and forgiving
- And 10 more challenging words!

## 📝 Data Format

Vocabulary words are stored in `vocabulary.json` in a structured format that's easy to extend:

```json
{
  "hard_vocabulary": [
    {
      "word": "Example",
      "pronunciation": "/ɪɡˈzɑːmp(ə)l/",
      "part_of_speech": "noun",
      "definition": "A thing characteristic of its kind",
      "example": "This is an example sentence.",
      "synonyms": ["instance", "case", "illustration"],
      "difficulty": "intermediate"
    }
  ]
}
```

## 🎯 Who Is This For?

This tool is perfect for:
- Students preparing for SAT, GRE, GMAT, or TOEFL exams
- English language learners advancing to higher levels
- Anyone looking to expand their vocabulary with sophisticated words
- Test prep and exam preparation

## 🔧 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## 📈 Extending the Vocabulary

To add more words, simply edit `vocabulary.json` and add new entries following the existing format. The program will automatically load all words from the file.

---

**단어장** - Hard vocabulary specialized for exam reading comprehension
