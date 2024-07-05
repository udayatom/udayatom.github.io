Entities are structured pieces of information inside of a user message.

An entity can be any important detail that your assistant could use later in a conversation.
* Number
* Dates
* Country names
* Product names 
  
![image](assets/Pasted%20image%2020230109074904.png)
    
Training data for entity extraction should be included in your nlu.xml file.


**There are 3 ways entities can be extracted in Rasa:**
1) Using pre-build models:
	- Duckling for extracting numbers, dates, url, email addresses
	- SpaCy - for extracting names, product names, locations etc
	 ![[Pasted image 20230109075342.png]]

  2) Using Regex:
	  - For entities that match a specific pattern(Eg: phone number, post codes)
	    ![[Pasted image 20230109075523.png]]

   3) Using machine learning:
	   - For extracting custom entities
	     ![[Pasted image 20230109075746.png]]

 **The output of the entity extraction**
 Output is the snippet of JSON which contains the details of:
	 - Entity category("City")
	 - Entity value("New York City")
	 - Confidence levels
	 - The component that extracted the entity. 
	   ![[Pasted image 20230109082809.png]]
**Apart from Machine learning, provides Synonyms**
  Synonyms can be used to map the extracted values to a single standardized value. 
	![[Pasted image 20230118082355.png]]
![[Pasted image 20230118082532.png]]

**Lookup Tables**

	Lookup tables are lists of words used to generate case-sensitive regular expression patterns.
	
	![[Pasted image 20230118082831.png]]

**Entity Roles**

	Entity Roles and Groups allow you to add more details to your entities.
	
	Roles: Allow you to define the roles of the entities of the same groups.

![[Pasted image 20230118083416.png]]


	Groups: Allow you to put extracted entities under a specific group.

![[Pasted image 20230118083656.png]]

**Entity Roles can be configured to influence the conversation flow**
	If you would like to entity roles to influence the conversation flow, you should include the entity roles in your stories, For ex:
	![[Pasted image 20230118084109.png]]
