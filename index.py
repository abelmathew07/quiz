import random

# Define the set of questions and options
questions = [
    {
        'question': 'PCI stands for _______',
        'options': ['a) Peripheral Component Interconnect', 'b) Peripheral Computer Internet', 'c) Processor Computer Interconnect', 'd) Processor Cable Interconnect'],
    },
    {
        'question': 'Which is the 3 types of expansion slot',
        'options': ['a) PCI', 'b) AGP', 'c) ISA', 'd) All of these'],
    },
    {
        'question': 'Which of these is a storage device?',
        'options': ['a) CD ROM', 'b) Register', 'c) Cache memory', 'd) All of these'],
    },
    {
        'question': 'Full form of USB?',
        'options': ['a) Universal Serial Bus', 'b) Universal Service Bus', 'c) Universe Series Bus', 'd) None of the above'],
    },
    {
        'question': 'a: RAM is a volatile memory\nb: ROM is a volatile memory',
        'options': ['a) Both', 'b) Only A', 'c) Only B', 'd) None'],
    },
    {
        'question': 'Computer Joystick is an',
        'options': ['a) Input device', 'b) Output device', 'c) Processing device', 'd) Memory device'],
    },
    {
        'question': 'Which is the first microprocessor?',
        'options': ['a) Intel 4004', 'b) Intel 3005', 'c) Intel Pentium 1005', 'd) Intel 286'],
    },
    {
        'question': 'Which device is used to separate sound output picked up by separate microphones in a TV receiver or DVD player in surround sound state stereo receiver?',
        'options': ['a) Encoder', 'b) Multiplexer', 'c) Transformer', 'd) Decoder'],
    },
    {
        'question': 'ZIF stands for _______',
        'options': ['a) Zero instrumentation force', 'b) Zero insertion force', 'c) Zero insulation force', 'd) None of the above'],
    },
    {
        'question': 'Hard disk can have ______ heads.',
        'options': ['a) One', 'b) Two', 'c) More than two', 'd) Only one'],
    },
]

# Shuffle the questions randomly
random.shuffle(questions)

# Print the shuffled questions and options
for i, question in enumerate(questions, start=1):
    print(f"{i}. {question['question']}")
    for option in question['options']:
        print(f"   {option}")
    print()
