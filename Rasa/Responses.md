Responses are simple messages that your assistant can send back to your users.
![image](/assets/Pasted%20image%2020230123081324.png)

Response templates are defined in the domain.yml file.
![image](/assets/Pasted%20image%2020230123081533.png)

Creating multiple responses

Your can include more than one possible response for a specific template. Rasa will the randomly select which response to pick.
![image](/assets/Pasted%20image%2020230123081740.png)

**Using variables**

You can create more dynamic responses by including [[slots]] in the responses.
![image](/assets/Pasted%20image%2020230123082035.png)

![image](/assets/Pasted%20image%2020230123082317.png)

![image](/assets/Pasted%20image%2020230123082543.png)

Adding buttons
You can enrich your assistant's responses by including buttons for specific options. You can configure the text that is visible on the buttons as well as the payload that is being sent to Rasa after a specific button is pressed.
Buttons can send the entities to the Rasa assistant backend.

![image](/assets/Pasted%20image%2020230124180659.png)

Custom Payload

If you prefer, you can get your assistant to send a custom payload to your frontend.

![image](/assets/Pasted%20image%2020230124223453.png)

Channel specific responses
You can define responses that will be sent to a specific output channel
![image](/assets/Pasted%20image%2020230124223700.png)

Training your assistant to use the responses
To enable your assistant to actually use the defined responses, you have to include them into your training stories.
![image](/assets/Pasted%20image%2020230124223802.png)
