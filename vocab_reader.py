#!/usr/bin/env python3
"""
English Hard Vocabulary Reader for Exam Preparation

This script helps users learn difficult English vocabulary words
commonly found in standardized tests (SAT, GRE, TOEFL, etc.)
"""

import json
import random
import sys
from typing import List, Dict

def load_vocabulary(file_path: str = 'vocabulary.json') -> List[Dict]:
    """Load vocabulary from JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['hard_vocabulary']
    except FileNotFoundError:
        print(f"Error: {file_path} not found!")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}")
        sys.exit(1)

def display_word(word_data: Dict, show_answer: bool = False):
    """Display a vocabulary word with its details"""
    print("\n" + "="*60)
    print(f"WORD: {word_data['word']}")
    print(f"Pronunciation: {word_data['pronunciation']}")
    print(f"Part of Speech: {word_data['part_of_speech']}")
    print(f"Difficulty: {word_data['difficulty'].upper()}")
    print("="*60)
    
    if show_answer:
        print(f"\nDefinition: {word_data['definition']}")
        print(f"\nExample: {word_data['example']}")
        print(f"\nSynonyms: {', '.join(word_data['synonyms'])}")
    else:
        print("\n[Definition hidden - press Enter to reveal]")

def quiz_mode(vocabulary: List[Dict]):
    """Interactive quiz mode"""
    print("\n📚 QUIZ MODE - Test Your Vocabulary Knowledge!")
    print("="*60)
    
    random.shuffle(vocabulary)
    score = 0
    
    for i, word_data in enumerate(vocabulary, 1):
        print(f"\n\nQuestion {i}/{len(vocabulary)}")
        display_word(word_data, show_answer=False)
        
        input("\nPress Enter to see the answer...")
        display_word(word_data, show_answer=True)
        
        while True:
            response = input("\nDid you know it? (y/n/q to quit): ").lower().strip()
            if response in ['y', 'n', 'q']:
                break
            print("Please enter 'y' for yes, 'n' for no, or 'q' to quit")
        
        if response == 'q':
            break
        elif response == 'y':
            score += 1
            print("✓ Great job!")
        else:
            print("✗ Keep studying!")
    
    print(f"\n\n{'='*60}")
    print(f"FINAL SCORE: {score}/{i}")
    print(f"Percentage: {(score/i)*100:.1f}%")
    print("="*60)

def study_mode(vocabulary: List[Dict]):
    """Study mode - browse all words"""
    print("\n📖 STUDY MODE - Learn Hard Vocabulary")
    print("="*60)
    
    for i, word_data in enumerate(vocabulary, 1):
        print(f"\n\nWord {i}/{len(vocabulary)}")
        display_word(word_data, show_answer=True)
        
        if i < len(vocabulary):
            response = input("\nPress Enter for next word (or 'q' to quit): ").strip().lower()
            if response == 'q':
                break

def filter_by_difficulty(vocabulary: List[Dict], difficulty: str) -> List[Dict]:
    """Filter vocabulary by difficulty level"""
    return [word for word in vocabulary if word['difficulty'].lower() == difficulty.lower()]

def search_word(vocabulary: List[Dict], search_term: str):
    """Search for a specific word"""
    for word_data in vocabulary:
        if word_data['word'].lower() == search_term.lower():
            display_word(word_data, show_answer=True)
            return
    print(f"\n❌ Word '{search_term}' not found in vocabulary list.")

def main():
    """Main function"""
    print("="*60)
    print("    HARD VOCABULARY READER FOR EXAM PREPARATION")
    print("    Specialized for Difficult English Words")
    print("="*60)
    
    vocabulary = load_vocabulary()
    
    while True:
        print("\n\nMAIN MENU:")
        print("1. Study Mode - Browse all words")
        print("2. Quiz Mode - Test yourself")
        print("3. Filter by Difficulty")
        print("4. Search for a word")
        print("5. Show Statistics")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            study_mode(vocabulary)
        elif choice == '2':
            quiz_mode(vocabulary)
        elif choice == '3':
            print("\nDifficulty Levels:")
            print("1. Intermediate")
            print("2. Advanced")
            print("3. Expert")
            diff_choice = input("Select difficulty (1-3): ").strip()
            
            diff_map = {'1': 'intermediate', '2': 'advanced', '3': 'expert'}
            if diff_choice in diff_map:
                filtered = filter_by_difficulty(vocabulary, diff_map[diff_choice])
                print(f"\nFound {len(filtered)} words at {diff_map[diff_choice]} level")
                study_mode(filtered)
            else:
                print("Invalid choice")
        elif choice == '4':
            search_term = input("Enter word to search: ").strip()
            search_word(vocabulary, search_term)
        elif choice == '5':
            print("\n📊 VOCABULARY STATISTICS")
            print("="*60)
            print(f"Total words: {len(vocabulary)}")
            
            by_difficulty = {}
            for word in vocabulary:
                diff = word['difficulty']
                by_difficulty[diff] = by_difficulty.get(diff, 0) + 1
            
            for diff, count in sorted(by_difficulty.items()):
                print(f"{diff.capitalize()}: {count} words")
        elif choice == '6':
            print("\n👋 Thank you for studying! Keep up the great work!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
