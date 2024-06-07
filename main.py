
article="""What is artificial intelligence (AI)? Everything you need to know
By
Nicole Laskowski, Senior News DirectorLinda Tucci, Industry Editor -- CIO/IT Strategy
What is AI?
Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems. Specific applications of AI include expert systems, natural language processing, speech recognition and machine vision.

How does AI work?
As the hype around AI has accelerated, vendors have been scrambling to promote how their products and services use it. Often, what they refer to as AI is simply a component of the technology, such as machine learning. AI requires a foundation of specialized hardware and software for writing and training machine learning algorithms. No single programming language is synonymous with AI, but Python, R, Java, C++ and Julia have features popular with AI developers.

In general, AI systems work by ingesting large amounts of labeled training data, analyzing the data for correlations and patterns, and using these patterns to make predictions about future states. In this way, a chatbot that is fed examples of text can learn to generate lifelike exchanges with people, or an image recognition tool can learn to identify and describe objects in images by reviewing millions of examples. New, rapidly improving generative AI techniques can create realistic text, images, music and other media.

AI programming focuses on cognitive skills that include the following:

Learning. This aspect of AI programming focuses on acquiring data and creating rules for how to turn it into actionable information. The rules, which are called algorithms, provide computing devices with step-by-step instructions for how to complete a specific task.
Reasoning. This aspect of AI programming focuses on choosing the right algorithm to reach a desired outcome.
Self-correction. This aspect of AI programming is designed to continually fine-tune algorithms and ensure they provide the most accurate results possible.
Creativity. This aspect of AI uses neural networks, rules-based systems, statistical methods and other AI techniques to generate new images, new text, new music and new ideas.
Differences between AI, machine learning and deep learning
AI, machine learning and deep learning are common terms in enterprise IT and sometimes used interchangeably, especially by companies in their marketing materials. But there are distinctions. The term AI, coined in the 1950s, refers to the simulation of human intelligence by machines. It covers an ever-changing set of capabilities as new technologies are developed. Technologies that come under the umbrella of AI include machine learning and deep learning.

Machine learning enables software applications to become more accurate at predicting outcomes without being explicitly programmed to do so. Machine learning algorithms use historical data as input to predict new output values. This approach became vastly more effective with the rise of large data sets to train on. Deep learning, a subset of machine learning, is based on our understanding of how the brain is structured. Deep learning's use of artificial neural network structure is the underpinning of recent advances in AI, including self-driving cars and ChatGPT.

Why is artificial intelligence important?
AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design.

AI has become central to many of today's largest and most successful companies, including Alphabet, Apple, Microsoft and Meta, where AI technologies are used to improve operations and outpace competitors. At Alphabet subsidiary Google, for example, AI is central to its search engine, Waymo's self-driving cars and Google Brain, which invented the transformer neural network architecture that underpins the recent breakthroughs in natural language processing.


What are the advantages and disadvantages of artificial intelligence?
Artificial neural networks and deep learning AI technologies are quickly evolving, primarily because AI can process large amounts of data much faster and make predictions more accurately than humanly possible.

While the huge volume of data created on a daily basis would bury a human researcher, AI applications using machine learning can take that data and quickly turn it into actionable information. As of this writing, a primary disadvantage of AI is that it is expensive to process the large amounts of data AI programming requires. As AI techniques are incorporated into more products and services, organizations must also be attuned to AI's potential to create biased and discriminatory systems, intentionally or inadvertently.

Advantages of AI
The following are some advantages of AI.

Good at detail-oriented jobs. AI has proven to be just as good, if not better than doctors at diagnosing certain cancers, including breast cancer and melanoma.
Reduced time for data-heavy tasks. AI is widely used in data-heavy industries, including banking and securities, pharma and insurance, to reduce the time it takes to analyze big data sets. Financial services, for example, routinely use AI to process loan applications and detect fraud.
Saves labor and increases productivity. An example here is the use of warehouse automation, which grew during the pandemic and is expected to increase with the integration of AI and machine learning.
Delivers consistent results. The best AI translation tools deliver high levels of consistency, offering even small businesses the ability to reach customers in their native language.
Can improve customer satisfaction through personalization. AI can personalize content, messaging, ads, recommendations and websites to individual customers.
AI-powered virtual agents are always available. AI programs do not need to sleep or take breaks, providing 24/7 service.
Disadvantages of AI
The following are some disadvantages of AI.

Expensive.
Requires deep technical expertise.
Limited supply of qualified workers to build AI tools.
Reflects the biases of its training data, at scale.
Lack of ability to generalize from one task to another.
Eliminates human jobs, increasing unemployment rates."""

import streamlit as st
from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")



st.title("Text Summarizer using Transformers")
input_text=st.text_area("Please enter the text here:")
submit=st.button("Summarize")

summary=summarizer(input_text, max_length=200, min_length=50, do_sample=False)
st.write(summary[0]['summary_text'])
