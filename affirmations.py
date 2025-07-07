name = input("What shall I call you today? : ")
print("\nHow are you feeling,",name,"?")
print("1. Happy")
print("2. Sad")
print("3. Angry")
print("4. Meh")
choice= int(input("\nChoose your emotion: "))
rate= int(input("\nHow much, on a scale of 1 to 5? (1 being just feeling the shadow of it and 5 being feeling it in your bones):"))

if choice not in {1,2,3,4} or not (1<=rate<=5):
 print("\nSeek a therapist🙏")
 exit() 

affirm = {
        1: {  # Happy
            1: "When you can't find sunshine, be the sunshine.",
            2: "I'm proud of my progress, no matter how small.",
            3: "Abundance surrounds me, and I'm grateful.",
            4: "I'm confident, calm, and successful.",
            5: "I am {name}—if not me, then who? 🌟",
        },
        2: {  # Sad
            1: "This feeling will pass.",
            2: "I've survived worse before; I'll survive this too.",
            3: "I'm doing the best I can, and that is truly enough.",
            4: "I am not alone—there are people who care about me.",
            5: "I am {name}. I don't break this way—never have, never will. 💪",
        },
        3: {  # Angry
            1: "I am immune to others' opinions.",
            2: "I don't let situations or people control me.",
            3: "I am more powerful than anyone who threatens my peace.",
            4: "I choose to let go of anger and choose myself instead.",
            5: "I am {name}. I'm better than this—forever. 🔥",
        },
        4: {  # Meh
            1: "I have everything I need to make today a great day.",
            2: "I let go of limiting beliefs and embrace all that I am.",
            3: "I have time. I have space. I have permission to begin gently.",
            4: "I am capable of achieving great things.",
            5: "I am {name}. I don't wait for opportunities—I create them. 🚀",
        },
    }

quote= affirm[choice][rate].format(name=name)
print("\n************\nTake a deep breathe and repeat after me...")
print(f"\n💌 {quote} \n************\n")
