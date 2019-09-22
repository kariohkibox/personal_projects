# The script of the game goes in this file.

# The game starts here.

label chapter1:

    # Shows a background.

    scene bg circle_outside_sunset
    with fade

    "I walked near the entrance to CiRCLE, feeling my heart rate increase."
    "I've been here so many times, but today...today is different..."
    "Usually Roselia practices alone, without anyone watching or listening. Even Marina-san tends to leave us alone."
    "But today...someone from another band will be visiting us..."
    "It came up at our last practice..."

    scene bg circle_inside
    with dissolve

    # plays music
    play music "03_Normal.mp3"

    show yukina uniform idle at center

    yukina "Good work today, everyone. I believe the new song is coming together well."

    show yukina uniform idle:
        linear 0.3 xpos 0.2
    pause 0.5
    show sayo uniform smile at right

    sayo "Hmm..."
    yukina "Sayo? Do you have something to comment on?"
    sayo "I feel like something is missing from our new piece."
    yukina "I see. Any suggestions?"

    show sayo uniform smile:
        linear 0.3 xpos 1.1
    pause 0.2

    show lisa uniform wave at center
    with dissolve

    lisa "Oh, I've got an idea! Sorry to butt in∼"
    yukina "It's fine, Lisa. Your opinion is valuable, after all."
    lisa "Thanks∼! Anyway, I was thinking we should have someone come watch us and give some feedback."
    lisa "I know the perfect person, too! So, if it's okay with everyone..."

    scene bg circle_outside_sunset
    with dissolve
    stop music fadeout 0.5

    "..."
    "And that's how it happened."
    "Lisa only told Yukina who was coming, telling the rest of us that it would be a surprise..."

    unkchar "Hey..."

    # This ends the game.

    return
