Slots are assistant's memory. Slots enable your assistant to store important details and later use them in a specific context.
![image](/assets/Pasted%20image%2020230120075604.png)

**Configuring slots**
Slots are defined inside of your domain.yml file.
![image](/assets/Pasted%20image%2020230120075725.png)

**Setting slots**

1. Using NLU
   ![image](/assets/Pasted%20image%2020230120075856.png)
2. Using [[Custom actions]]

**Influencing the conversation**

    Slots can be configured to influence the flow of the conversation. How and when this should happen depends on the type of the slot.

![image](/assets/Pasted%20image%2020230120080203.png)

influence_conversation = true
influence_conversation = true configuration defines that the slot will influence how the dialogue management model makes the prediction for the next action. Depending on the type of the slot the flow can be influenced by the value of the slot or whether the value of this slot is present.
![image](/assets/Pasted%20image%2020230120080447.png)

influence_conversation = false
influence_conversation = false configuration defines that the slot would not influence the flow of the conversation and should only be used for storing the value of the slot.
![image](/assets/Pasted%20image%2020230120080757.png)

**Configuring the stories**
If your slots are configured to influence the flow of the conversation, you have to include them in your training stories. For example:

![image](/assets/Pasted%20image%2020230120080819.png)

**Slot mappings**
Slot mappings allow you to define how each slot will be filled in. Slot mappings are applied after each user message.
![image](/assets/Pasted%20image%2020230120081754.png)

Slot mappings:from_text
The from_text slot mappings will use the text of the last user message to fill in the slot.

![image](/assets/Pasted%20image%2020230120081841.png)

Slot mappings:from_intent
The Slot mappings:from_text slot mapping fills in the slot with a specific defined value if a specific defined value if a specific intent is predicted.
![image](/assets/Pasted%20image%2020230120082113.png)

Slot mappings:from_trigger_intent

The from_trigger_intent mapping will fill slot with a specific defined value if a form is activated by a user message with a specific intent.

![image](/assets/Pasted%20image%2020230120082206.png)

Slot mappings:custom

If none of the predefined slot mappings fit your use case, you can create custom slot mapping using slot validation actions.

![image](/assets/Pasted%20image%2020230120082414.png)

**Slot type:**

1. Text
   Slot type text can be used to store any text information. It can influence the conversation based on whether or not the slot has been set.
   ![image](/assets/Pasted%20image%2020230123080055.png)
   Eg: Flight ticket conversation

2. boolean
   Slot type boolean can be used to store information that can get the values True or False.

![image](/assets/Pasted%20image%2020230123080210.png)

3. categorical
   Slot type categorical can be used to store values that can get one of the possible N values.
   ![image](/assets/Pasted%20image%2020230123080451.png)
4. float
   Slot type float can be used to store numerical values.
   ![image](/assets/Pasted%20image%2020230123080541.png)

5. list
   Slot type list can be used to store a list of values. When configured, only the presence of the slot can have influence on the flow of the conversation.

   ![image](/assets/Pasted%20image%2020230123080658.png)

6. any
   Slot type any can be used to store any arbitrary values. Slots of this type don't have any influence on the conversation flow which means that the value and the presence of the slot doesn't have any influence on how the conversation goes.
   ![image](/assets/Pasted%20image%2020230123080950.png)

Additional configurations: initial_value
You can set a default initial value to your slot by configuring the initial_value parameter. The value will be assigned to the slot from the beginning of the conversation and can be reset later on by NLU or custom action.
![image](/assets/Pasted%20image%2020230123081220.png)
