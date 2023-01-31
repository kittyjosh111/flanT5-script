Some scripts to do text generation using FlanT5 and Hugging Face Transformers. Ensure you have enough RAM to run these. One way to find out is to just try running them. Also, the scripts only use CPU as they were originally run on Oracle Cloud's Free Tier, which does not have GPU support.

First use pip to install the ```requirements.txt```, then you can select which script to run. It will ask you for your prompt. Small, middle, and large indicate larger lengths and temperature values in their respective orders. Thus, the large script takes the longest to complete, and the fast is the shortest.

Examples are as follows. I am using venv on ubuntu with the 4 core, 24 GB RAM machine from Oracle Cloud. Both Fast and Middle took less than a minute to run. The Large option took at least five minutes to run.

*Fast:*
```
(venv) ubuntu@oracle:~/dev/flanT5-script$ python3 flanT5_fast.py 
Put in your prompt: How was your day today?
It was a good day for me because I didn't have to go to work today.
```

*Middle:*
```
(venv) ubuntu@oracle:~/dev/flanT5-script$ python3 flanT5_middle.py 
Put in your prompt: How was your day today?
It was a good day for me because I didn't have to go to work today and the weather was nice outside.
```

*Large:*
```
(venv) ubuntu@matrix:~/dev/flanT5-script$ python3 flanT5_large.py 
Put in your prompt:How was your day today?
It was a good day for me because I didn\'t have to go to work today and the weather was nice. My favorite part of the day was going to the park with my dog. We had a great time at the park. Then it was back to school, but not as busy as usual. There were lots of things to do in our neighborhood. Today we went on a bike ride around town. That was really fun. Our teacher gave us a lot of tips about how to be safe when riding your bike. They also taught us some new words that we don\'t know yet. All in all, it was a pretty good day overall. Thank you so much for sharing this wonderful day with us. Have a great day! Bye! bye! Goodnight! Blessings! And thanks for reading! See you tomorrow! Love you! God bless! Happy Birthday! Thanks for stopping by! Be sure to check out www.myspace.com/mommygoddesstoday http://www.facebook.com/MommyGoddesstoDayTwitter.com/MySpace?fref=http://www.instagram.com/melodygoddessestoday&amp;hashtag=MOMMY_GODDESSTODAY TWITTER-GIVEAWAY AND LIKE US ON FACEBOOK AT MOMMYGODDESSODAYTWITTER GIVEAWAY TODAY @ https://www.youtube.com/memorygoddessaystoday You can use the hashtag #BirthdayCelebrityHappyBirTHdayChildhoodOfHappinessOnThursdayJuly20th@gmail.com If you have any questions or comments, please feel free to leave them in the comment section below. Your feedback is very important to us and will help us better serve you next year! Best Wishes! ||||| This post may contain affiliate links. Please read our disclaimer page for more information. These are external links and we are not responsible for their content. When you click on one of these links, you are agreeing to our terms and conditions. Any purchases made through these links are solely between you and Mommy GoddessToday.com. Mommy GodgesToday.com makes no representations or warranties regarding the content of its web site (the "Website"). Mommy GodiesToday.com has no control over the content of third party web sites linked from this Site. Copyright <unk> 2013 Mommy Godies Today. All Rights Reserved. Website Design by Hostess Digital Marketing Services Inc. May Not Be Reproduced Or Republished In whole or in part without prior written permission. No part of this website may be reproduced or transmitted in any form or by any means without prior written consent. Visit Mommy GoliesToday.com for more information. Follow Us On Twitter @ mommygodiestoday...and Like Us On Facebook At facebook.com/MotherGodiesTodayWelcomeToMommyDogDayTweetsAndThanksforReadingOurTermsAndConditionsThisWebSiteMayNotBeReprintedWithOutPresentAuthorizedSponsorFrameworkInTheForm Of
```

Feel free to modify the config values for the text generation. You can find them in the beginning block of the python scripts:
```
min_length=20
max_new_tokens=125
length_penalty=1.2
num_beams=5
no_repeat_ngram_size=5
temperature=0.9
top_k=75
top_p=0.9
repetition_penalty=3.
```
