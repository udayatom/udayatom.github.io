[[Responses]] - These are the things the assistant can say to users

Intents - There are categories of things user say

[[Slots]] - These are variables remembered over the course of a conversation.

[[Entities]] - There are pieces of information extracted from incoming text

Forms and Actions: These add application logic and extend what your assistant can do.

Responses: 

```
responses:  
  utter_greet:  
  - text: "Hey! How are you?"  
  
  utter_cheer_up:  
	- text: "Here is something to cheer you up:"  
	  image: "https://i.imgur.com/nGF1K8f.jpg"
```

**Adding variation**

```
responses:  
  utter_greet:  
  - text: "Hey! {name}. How are you?"  
  - text: "Hey! {name}. How is your day going?"  
```
 Here when response triggered, randomly will pick the statement.{name} will be filed with value. other wise return 'none'.
 
**Responses: Buttons and Images**

```
responses:  
  utter_greet:  
  - text: "Hey! How are you?"  
    buttons:
    -title: "Great"
	 payload:"/mood_great"
	-title: "Super"
	 payload:"mood_super"
  utter_cheer_up
  -text:"Heris hte image"
   image:"image_url"
```

Responses: Channel specific responses
```
responses:
  utter_askgame:
  -text: "Which game would you like to play on slack?"
   channel:"Slack"
  -text: "Which game would you like to play?" 
```

**Intents**
	Intents are talks to the assistant, based the user's input classified by the NLU. To connect with proper intent.
```
intents:
 - affirm
 - deny
```

**What is "data" for a Rasa Project?**
1) The text data used to pretrain any models or features you're using(eg: Language models, word embeddings, etc)
2) User-generated text(Eg: Saying hello in multiple form)
3)  Patterns of conversations(Eg: Customer support logs)

**How should conversations with your chatbot go?**
**1) Stories**
   Training data to teach your assistant what it should do next.
   1) If you have conversational data start with the patterns.
   2) Generating your own conversational patterns: 
	 It's easiest to use interactive learning to create stories
	  1) Start with common flows,  "happy paths"
	  2) Then add common errors/digressions
   3) Once your model is trained:
	   Add more data from user conversations.
 
 rasa_project/data/stories.yml
 ```
 stories:
	-story: happy path
	 steps:
	 -intent: greet
	 -action: utter_greet
	 -intent: mood_great
	 -action: utter_happy 
```

**OR Statments**
```
stories:
- story: newsletter signup with OR
 steps:
 -intent: signup_newsletter
 -action: utter_ask_confirm_signup
 -or
  -intent: affirm
  -intent: thanks
 -action: action_signup_newsletter 
```

**Checkpoints**
```
stories:
- story: beginning of conversation
  steps:
  -intent: greet
  -action: utter_greet
  -intent: goodbye
  -action: utter_goodbye
  -checkpoint: ask_feedback
```

**We can start new stories from the check point**
```
- story: user provides feedback
  steps:
  - checkpoint: ask_feedback
  - action: utter_ask_feedback
  - intent: inform
  - action: utter_thank_you
  - action: utter_anything_else
  
- story: user doesn't have feedback
  steps:
  - checkpoint: ask_feedback
  - action: utter_ask_feedback
  - intent: deny
  - action: utter_no_problem
  - action: utter_anything_else
  
```

**2) Rules**
 A way to describe short piece of conversation that always go the same way
 rasa_project/data/rules.yml
 ```
 rules:
	 - rule: Greeting Rule
	  steps:
	  -intent: greet
	  -action: utter_greet
```

 3) Intents
 rasa_project/data/nlu.yml 
```
nlu:
	- intent: greet_smalltalk
	  examples:
	  - hi
	  - hello
```
* If we have data
* Modified content analysis:
	* Go through data by hand and assign each datapoint to a group
	* If no existing group fits, add a new one
	* At given intervals go through your groups and combine or separate them as needed
	* Start with 2-3 passes through your dataset
* If you don't have data
	* Start with most common intent
		  - most people want to do the same thing
		  - Use the experts in your institution
	  - Start with the smallest possible number of intents
	  - Everything else goes in an out of scope intent 
		    - If your assistant can't handle something, give users an escape hatch right away   
* Why fewer intents?
	 * Older style of conversational design
		     - You need an intent for everything your user might want to do
	* Rasa style CDD
			- You only need to start with the most popular, important intents & a way to handle things outside them
			- Continue to build from there if that's what users need
	- Human reasons
			- More intents = more training data, maintenance, documentation
			- More intents = annotation more difficult
	* ML reasons
			- Transformer classifiers scale linearly with the # of classes
			- Entity extraction(Especially. with very lightweight rule-based system like Duckling) is often faster

   * Paring down intents
	   * Don't use intents as a way to store infromation
		       - Storing information = [[slots]]
	   * Do a lot of same tokens show up in training data for two intents?
			 - Consider if they can be combined
			 - ![[Pasted image 20230108213402.png]]

  * Training data for an intent
	- User-generated > Synthetic
	- Each utterance should unambiguosly match to a single intent
			- You can verify this using human sorting & inter-rather reliability
	* Is an utterance ambiguous?
			- Use end to end instead(the raw text as training data w/out classifying it)
			- ![[Pasted image 20230108214025.png]]
			- ![[Pasted image 20230108214133.png]]
		
		
		<audio controls>

<source src="/assets/jazzyfrenchy.mp3" type="audio/mpeg">

Your browser does not support the audio element.

</audio>