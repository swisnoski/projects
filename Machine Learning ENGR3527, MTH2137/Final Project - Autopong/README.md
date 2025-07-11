# autopong

A repository created to host and share the my final project for MTH2137/ENGR2137 Machine Learning at Olin College. 

Autopong is a bot that has been trained using reinforcement learning to excel in OpenAI Gymnasium's pong environment. For trainging, I used a Deep-Q learning model from stablebaselines3, and built my own model using tensor flow. Each model was trained locally for 36 and 24 hours respectively and then compared to a randomized model. While both models improved significantly compared to a randomized model, neither acheived true mastery: 
* the stablebaselines 3 model usually won by 5-10 points
* the tensorflow model I bult usually lost by 5-10 points
* the randomized model usually lost by 20-21 points


The majority of my work was completed in a jupyter notebook in the format of a technical essay, included above. 
