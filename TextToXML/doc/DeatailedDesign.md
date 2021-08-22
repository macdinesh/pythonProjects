#Problem Statement 
Text documents, such as tweets, are usually composed of topically coherent text data, which
within each topically coherent data, one would expect that the word usage demonstrates more
consistent lexical distributions than that across the data-set. A linear partition of texts into topic
segments can be used for text analysis tasks, such as passage retrieval in IR (information
retrieval), document summarization, recommender systems, and learning-to-rank methods.

# Task 1: Parsing Text Files (%60)

This assessment touches the very first step of analyzing textual data, i.e., extracting data
from semi-structured text files. Each student is provided with a data-set that contains
information about cryptocurrency related tweets (please find your own directory for Task1 from
here). Note that if you mount Google Drive in the Colab environment (as explained in the
tutorials) you can access your own file directly with a unique URL (e.g.,
“/content/drive/Shareddrives/FIT5196-s2-2021-tutorials/Assessment 1/Task1 datasets/<stdno>.txt” ). Each
text file contains information about the tweets, i.e., “user name”, “user code”, “user
description”, “number of followers”, “whether or not the user account is verified”, “date
of the tweet”, and the “tweet text”. Your task is to extract the data from the text file and
transform the data into a XML format with the following elements:
1. users: this tag wraps all the users
2. user: this tag wraps all the tweets from a particular user and keeps the meta data for
each user such as number of followers, verified or not, user description etc. If a user has
multiple tweets, the meta data of the latest tweet (i.e., the tweet with the most
recent date) must be used.
3. Tweets: wraps all the tweets of a specific user
4. tweet: for each user, this tag represents the text of the user tweet
The XML file must be in the same structure as the sample solution provided here. Please note
that, as we are dealing with large datasets, the manual checking of outputs is impossible
and output files would be processed and marked automatically therefore, any deviation
from the XML structure (i.e. task1_sample_output.xml) such as wrong key names which
can be caused by different spelling, different upper/lower case, etc., wrong hierarchy, not
handling the XML special characters etc. will result in receiving zero for the output mark.
(hint: run your code on the provided sample input and make sure that your code results in the
exact same structure (not necessary content) as the sample output. You can also use web
applications such as xmlviewer to better understand the structure of the output.

# VERY IMPORTANT NOTE: 
The sample outputs are just for you to understand the
structure of the required output and the correctness of their content is not
guaranteed. So Please do not try to reverse engineer the outputs as it will fail to
generate the correct content.Please note that the re and os packages in Python are the only packages that you are allowed
to use for the task 1 of this assessment (e.g., “pandas” is not allowed!). Any other packages that
you need to “import” before usage is not allowed.
The output and the documentation will be marked separately in this task, and each carries its
own mark.

# Output
See sample.xml for detailed information about the output structure. The following must be
performed to complete the assessment.
● Designing efficient regular expressions in order to extract the data from your textual
dataset
● Storing and submitting the extracted data into an XML file,
<your_student_number>.xml following the format of sample.xml
● Explaining your code and your methodology in task1_<your_student_number>.ipynb
with all the cells’ outputs.
● A pdf file, “task1_<your_student_number>.pdf ”. You can first clean all the output in the
jupyter notebook task1_<your_student_number>.ipynb and then export it as a pdf file
then run all the codes again to make sure your ipynb file has all the outputs. This pdf will
be passed to Turnitin for plagiarism chec