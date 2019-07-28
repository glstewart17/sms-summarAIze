# sms-summarAIze
 Update summarAIze and use sms

The web application will write a nonsensical summary of just about any topic.
This version is reachable through sms messaging using twilio.
Just get a number, link it to the address, and message away.

This simple Flask application will take in any topic.
Wikipedia's API is then used to bring in an article related to the topic.
A self-made NLG will then produce one sentence on the subject.
The NLG is only trained by one wikipedia article at a time, so it is not overly accurate.
Thus, the majority of output is gramatically correct, but the content is fairly off.
Without more thorough training, the output will remain quite goofy. 

Example:

![Input Image](/example/SummarAIze Screenshot.jpg)
