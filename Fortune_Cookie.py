#Simulated a fortune cookie
#Display one of five unique fortunes at random

import random

cookies = [ 
    "No snowflake in an avalanche ever feels responsible.",
        "I cannot help you, for I am just a cookie.",
            "You will marry a professional athelete - if competitive eating can be considered a sport.",
                "You are not illiterate.",
                    "I see money is in your future... it is not yours though."
                    ]

print (random.choice(cookies))

input("\n\n Press Enter To Exit")
