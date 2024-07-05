What do we want virtual assistants to do?

- Pick up what the user wants from the assistant.
- Respond appropriately
- Send back appropriate message
- Send an email
- Make a calendar appointment
- Fetch relevant information from a database
- Check information from an API
- Calculate something specific

Where do they fit in?

![image](/assets/Pasted%20image%2020230125080436.png)

What does the custom code look like?

- def name() -> refers to stories, domain, rule file
- def run() -> we can write custom code, It receives the information from the Rasa NLU Service. Also send the responds.
- Send Messages -> Send message to the user
- Tracker objects contains the relevant data extracts from the conversation. It includes predictive intent, entities, conversation Sofar and also slot values.
- Custom action values also access the domani.yml file

![image](/assets/Pasted%20image%2020230125080715.png)

Example of a custom action
![image](/assets/Pasted%20image%2020230125081517.png)

![image](/assets/Pasted%20image%2020230125173832.png)

In rules.yml needs to defines the action.
![image](/assets/Pasted%20image%2020230125174129.png)
In domain.yml also needs to add the intent(inquire_time)
Needs to specify the entities(place).
![image](/assets/Pasted%20image%2020230125174155.png)
Needs to mention the action(action_tell_time) in the actions file. Same action needs to specify the actions.py
![image](/assets/Pasted%20image%2020230125174736.png)
Needs to enable the action_endpoint in the endpoints.yml
![image](/assets/Pasted%20image%2020230125182153.png)
