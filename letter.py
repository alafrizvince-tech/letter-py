import random
from datetime import datetime

def generate_love_letter(recipient_name: str, sender_name: str) -> str:
    """Generate a romantic love letter programmatically."""
    
    # Collections of romantic phrases
    openings = [
        f"My dearest {recipient_name},",
        f"To my beloved {recipient_name},",
        f"My sweet {recipient_name},"
    ]
    
    compliments = [
        "Your smile brightens even my darkest days.",
        "Your laugh is the most beautiful sound I know.",
        "Your kindness knows no bounds.",
        "Your eyes hold the warmth of a thousand suns.",
        "Your presence makes everything feel right."
    ]
    
    feelings = [
        "I find myself thinking of you constantly.",
        "Every moment with you feels like a dream.",
        "My heart races whenever I see you.",
        "You've become my greatest treasure.",
        "Life feels incomplete without you."
    ]
    
    promises = [
        "I promise to support you through everything.",
        "I vow to cherish you always.",
        "I will stand by your side, come what may.",
        "I dedicate myself to making you happy.",
        "Together, we can conquer the world."
    ]
    
    closings = [
        "Forever yours,",
        "With all my love,",
        "Eternally devoted,",
        "Always and forever,"
    ]
    
    # Build the letter
    letter = random.choice(openings) + "\n\n"
    
    letter += f"Today, I wanted to tell you how much you mean to me.\n\n"
    
    letter += random.choice(compliments) + " " + random.choice(compliments) + "\n\n"
    
    letter += random.choice(feelings) + " " + random.choice(feelings) + "\n\n"
    
    letter += random.choice(promises) + "\n\n"
    
    letter += random.choice(closings) + "\n"
    letter += sender_name + "\n\n"
    
    letter += f"Written with love on {datetime.now().strftime('%B %d, %Y')}"
    
    return letter


# Example usage
if __name__ == "__main__":
    # Customize these names
    recipient = "Your Beloved"
    sender = "Your Admirer"
    
    love_letter = generate_love_letter(recipient, sender)
    print(love_letter)
    
    # Optional: Save to file
    with open("love_letter.txt", "w") as f:
        f.write(love_letter)
    print("\n✉️ Love letter saved to 'love_letter.txt'")
