# Sentires-Guide
A quick guide to Sentires: Phrase-level Sentiment Analysis toolkit, SIGIR'14
> Zhang, Yongfeng, et al. [Do users rate or review? boost phrase-level sentiment labeling with review-level sentiment classification](http://yongfeng.me/attach/bps-zhang.pdf). SIGIR'14.

To obtain this tool, please follow the instructions at the bottom of this [page](http://yongfeng.me/code/).

## Introduction
The tool is quite meaningful to the research community, as many research papers are based on its results. However, we cannot directly obtain (feature, opinion, sentiment) triplets for each product review. Moreover, most people may be more familiar with Python rather than Java on which this tool was built. Therefore, I present my data processing steps here to help people quick obtain the results.

## Steps
- the folder "lei" and the file "run_lei.sh" must be placed in the tool's folder named "English-Jar" shown in the screenshot
- modify "0.format.py", so that your datasets can be processed in the right format of the tool's input
- modify "4.lexicon.linux" accordingly, as it contains absolute paths
- run the commands one by one in "run_lei.sh" (do not run this script, otherwise it may throw memory error)

## Results
You will find a file "lei/output/reviews.pickle" which is a python list, and each element is an python dict with the following keys:

'user',

'item',

'rating',

'text',

'sentence' # this one is a list of tuples and each tuple looks like (feature, adjective, sentence, score)
