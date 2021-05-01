# LTTS_Mini_ProjectPY_257137

## Defining a chatbot

An interface to get a task done via a text or voice based conversation with a robot, sometimes aided by a human. It’s simply not a machine masquerading as an individual, but actually a new interface after the GUI, in some circles being referred to as a CUI (Conversational User Interface).

A![0_XSTZ731bRBVf5FM-_](https://user-images.githubusercontent.com/81014114/116692323-cd29d400-a9d9-11eb-8c61-10d4716e5c07.png)

## Why?

For quering or order placement specification use cases, etc, the uses and requirement of a chatbot is limitless. Almost all businesses, whether service or product related use chatbots for quering, FAQs, and other consulting depending on the use case.


## How?

 Through Machine Learning algorithms and regular expressions, chatbots can learn appropriate answers to specific user queries over time, for which they no longer require training. But the actual impact of this miraculous technology can be witnessed only if the user is able to understand what the chatbot says and likes it. It’s like interacting with your user and the difference between saying “Comfortable & Luxurious 4 seater convertible car” v/s a “a contraption, powered by an turbo charged internal combustion engine and able to carry 4 objects of max 90 Kg each.” Well designed chatbots are always use-case driven and have a personality.
 
 # Building
 
 ## Preprocessing
To implement the chatbot, we will be using Keras, which is a Deep Learning library, NLTK, which is a Natural Language Processing toolkit, and some helpful libraries
 
All chatbots come under the NLP (Natural Language Processing) concepts. NLP is composed of two things:

NLU (Natural Language Understanding): The ability of machines to understand human language like English.

NLG (Natural Language Generation): The ability of a machine to generate text similar to human written sentences.

 ### Cleaning and formatting data 
 
Formating the data so that the data can be processed easily and only useful data is used to train the model.

The model cannot take the raw data. It has to go through a lot of pre-processing for the machine to easily understand. For textual data, there are many preprocessing techniques available. The first technique is tokenizing, in which we break the sentences into words.

By observing the intents file, we can see that each tag contains a list of patterns and responses. We tokenize each pattern and add the words in a list. Also, we create a list of classes and documents to add all the intents associated with patterns.

### Application
Using the GUI, chatbot can engage in conversation


 
 
