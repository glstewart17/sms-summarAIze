# SummarAIze

This simple Flask application will take in any topic and any number of sentences.
Wikipedia's API is then used to bring in an article related to the topic.
A self-made NLG will then produce an output of the proper length.
The NLG is only trained by one wikipedia article at a time, so it is not overly accurate.
Thus, the majority of output is gramatically correct, but the content is fairly off.
Without thorough training, the output will remain quite goofy. 

Example Input:

![Input Image](/example/input.PNG)

Example Output:

![Output Image](/example/output.PNG)
