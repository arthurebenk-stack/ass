schedule = {
    "monday": "🎨 3:30 PM - Art Club",
    "tuesday": "⚽ 4:00 PM - Soccer Practice",
    "wednesday": "🎹 3:45 PM - Piano Lesson",
    "thursday": "📚 3:30 PM - Homework Help & Library Time",
    "friday": "🎬 4:30 PM - Movie Night with Friends",
    "saturday": "🌳 10:00 AM - Park Day (No School!)",
    "sunday": "🛌 12:00 PM - Rest and Relax (No School!)"
}

def check_schedule():
    print("--- Welcome to the After-School Schedule Checker! ---")
    print("Type a day of the week to see your plans (or type 'quit' to exit).")
    
    while True:
        day = input("\nEnter a day: ").strip().lower()
        
        if day == "quit":
            print("Goodbye! Have a great after-school day!")
            break
            
        if day in schedule:
            print(f"Your plans for {day.capitalize()}: {schedule[day]}")
        else:
            print("❌ Oops! That doesn't look like a valid day. Please check your spelling.")

if __name__ == "__main__":
    check_schedule()
