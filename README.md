# Sentires-Guide
A quick guide to Sentires: Phrase-level Sentiment Analysis toolkit, SIGIR'14
> Zhang, Yongfeng, et al. [Do users rate or review? boost phrase-level sentiment labeling with review-level sentiment classification](http://yongfeng.me/attach/bps-zhang.pdf). Proceedings of the 37th international ACM SIGIR conference on Research & development in information retrieval. ACM, 2014.

To obtain this tool, please follow the instructions at the bottom of this [page](http://yongfeng.me/code/).

## Introduction
The tool is very meaningful to the IR research community, as many research works are built on top of its results. However, it may be difficult to obtain (feature, opinion, sentence, sentiment) quadruples for each product review, since it did implement such a function. Moreover, nowadays people are tend to be more familiar with Python rather than Java on which this tool was developed. Therefore, here I present our data processing steps in the following paper to help people quickly obtain the aforementioned quadruples from user reviews.
> Lei Li, Yongfeng Zhang, Li Chen. Generate Neural Template Explanations for Recommendation. CIKM'20. \[[Paper](https://lileipisces.github.io/files/CIKM20-NETE-paper.pdf)\] \[[Code](https://github.com/lileipisces/NETE)\]

## Steps
![](https://github.com/lileipisces/Sentires-Guide/folder-hierarchy.png)
- the folder "lei" and the file "run_lei.sh" must be placed in the tool's folder named "English-Jar" shown above
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
