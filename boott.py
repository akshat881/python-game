from chatterbot import ChatBot               # importing the chatbot.
from chatterbot.trainers import ListTrainer  # importing trainer for teaching the bot.
# importing objects of their respective classes for comparing the inputs, each has different way of comparing.
from chatterbot.comparisons import levenshtein_distance, jaccard_similarity, synset_distance
# importing response selection method for given input.
from chatterbot.response_selection import get_first_response
# declaring and defining the bot.
bot = ChatBot("Adam",
              read_only=True,  # self learning attribute
              logic_adapters=[  # This attribute defines logic-adapters to be used for response giving by bot.

                {

                    "import_path": "chatterbot.logic.BestMatch",
                    "default_response": "I am sorry, but I do not understand.",
                    "statement_comparison_function": levenshtein_distance,
                    "response_selection_method": get_first_response,
                    "maximum_similarity_threshold": 0.70
                },
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    "default_response": "I am sorry, but I do not understand.",
                    "statement_comparison_function": jaccard_similarity,
                    "response_selection_method": get_first_response,
                    "maximum_similarity_threshold": 0.70
                },
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    "default_response": "I am sorry, but I do not understand.",
                    "statement_comparison_function": synset_distance,
                    "response_selection_method": get_first_response,
                    "maximum_similarity_threshold": 0.70
                },
              ]
              )
bot.storage.drop()  # clearing the self learned database of bot.
# conversation list for bot to compare and select most of the output from.
conv = ["hi", "Hello There! I am Hint Bot. Do you need a hint for the question?"
              " One point will be deducted per hint.",
              "ok","Glad to help You",
               "hey", "Hello There! I am Hint Bot. Do you need a hint for the question?",
                      " One point will be deducted per hint.",
               "no", "Ok, Good Luck!",
               "nope", "Ok, Good Luck!",
               "nahi", "Acha, koi ni",
               "no thank you", "Ok, Good Luck!",
               "later", "Sure!",
               "question", "which one?",
               "q", "which question?",
               "how are you?", "I am good and how the same for you.",
               "please", "Sure, please type 'hint' in text box.",
               "yes", "Sure, please type 'hint' in text box. ",
               "thanks", "Good Luck ;)",
               "bad", ":(",
               "who are you?", "Your friendly Hint Bot :)",
               "you are?", "Your friendly Hint Bot :)",
               "?", "???",
               "...", "......?",
               "bye", "Bye Bye!",
        "QCODE1", "He is the God of High-School ",
        "QCODE2", "He wanted to be the god of this World",
        "QCODE3", "The Next Tiny Giant",
        "QCODE4", "Three sword style is best",
        "QCODE5", "He is the Attack Titan",
        "QCODE6", "Neither Girlfriend Nor Sister",
        "QCODE7", "The next King of the Pirates",
        "QCODE8", "Strongest AOT character ",
        "QCODE9", "Dual Wielding Skill",
        "QCODE10", "Jan ken gēmu - Rock Paper Scissors  ",
        "QCODE11", "Bungee Gum Expert ",
        "QCODE12", "Fire Breathing Technique",
        "QCODE13", "Family of Assassins",
        "QCODE14", "The Fifth Demon Slayer",
        "QCODE15", "Psychotic lover",
        "QCODE16", "Innocent in love",
        "QCODE17", "Tatania",
        "QCODE18", "END",
        "QCODE19", "100%",
        "QCODE20", "One for All ",
        "QCODE21", "Midoriya's Ultimate Rival",
        "QCODE22", "Caped Baldy",
        "QCODE23", "Symbol of Peace",
        "QCODE24", "Substitute Soul Reaper",
        "QCODE25", "Sin of Greed",
        "QCODE26", "The Demon Cyborg",
        "QCODE27", "Sin of Wrath",
        "QCODE28", "The Perfect Copy",
        "QCODE29", "Misdirection Expert",
        "QCODE30", "God of Flavours",
        "QCODE31", "Code Geass",
        "QCODE32", "The Eye-Patch",
        "QCODE33", "Two in one",
        "QCODE34", "Blank Never Lose",
        "QCODE35", "Peace can only be achieved by experiencing Pain",
        "QCODE36", "The Most Evil Uchiha",
        "QCODE37", "Destroyed the planet of Saiyans",
        "QCODE38", "The Best Detective",
        "QCODE39", "The Evil Genius",
        "QCODE40", "The Candy Lover",
        "QCODE41", "The Perfect Villain",
        "QCODE42", "Some People call him Tobi",
        "QCODE43", "The Uchiha Clan Massacre",
        "QCODE44", "Lord 7th",
        "QCODE45", "KA MEE HAA ME HAAA!!",
        "QCODE46", "The Saiyan Prince",
        "QCODE47", "The First SSJ2",
        "QCODE48", "The Last Uchiha",
        "QCODE49", "King of the Court",
        "QCODE50", "The Copy Ninja",

        ]

# command to train the bot by passing the bot to ListTrainer.
trainer = ListTrainer(bot)
trainer.train(conv)  # passing list to teach the bot.
