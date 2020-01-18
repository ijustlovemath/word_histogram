For use with grep-reddit or any other CLI utility, creates word histograms from stdin

## Example: histogram of all subreddits you've ever commented or posted in

python grep-reddit.py --user your_username --login your_username --all | grep -o "\/r\/\w*" | python ../word_histogram/word_hist.py 

