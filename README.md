# Spam-resistant Crowdsourcing of Accurate Cut-off Scores

As the number of responses to a survey increase, average values become more accurate, with errors and falsifications cancelling out. However, extreme (maximum/minimum) values turn unreliable, as mistakes and trolls become almost certain.

So, how do we solve this when, for instance, polling applicants to determine cut-off scores for university courses? Besides their score and alloted branch, have them also sumbit the branches they were denied. For each branch, at each possible score, tally the reported acceptances ($+1$) and rejections ($-1$).

<div align="center"><img src="https://github.com/user-attachments/assets/ac29885b-2777-4a54-9c81-3a3c6a0858aa" width="75%"><br>
<i>Idealized graph of the tallied acceptances and rejecttions at each score, for a particular course.<br>
The y-axis represents the tally and the x-axis the exam score. 280 is the cut-off for this particular course.</i></div><br>

The key property of the cut-off score is that there are a lot of positive y-values to its right (let their sum be $R$), and a lot of negative y-values to the left (let their sum be $L$). Thus $R-L$ is going to be at its maximum when computed about the cut-off point. This is a very robust property and is not easy to change via the addition of some untrue $\pm1\textsf{'s}$ to either side.

Now let the scores be $x$, and the y-value at a given score be $f(x)$.

When you go from $x_1$ to $x_2$ (ssuming all scores in between have zero y-value), $R$ decreases by $f(x_2)$ and $L$ increases by $f(x_1). Thus $R-L$ decreases by $f(x_2)+f(x_1)$.

$R-L$ for the leftmost score is simply the sum of all the y-values, and we can use the above formula to easily compute it for all scores.

## The Survey

[Here's](https://forms.gle/p1YCeHfxr6jHUgcg9) a survey for the institute [BITS Pilani](https://en.wikipedia.org/wiki/BITS_Pilani), India, which has three campuses – Pilani, Goa, and Hyderabad, and where admission is via the BITSAT examination. The survey contains three quesions:
* What is your final moderated BITSAT score?
* Which campus and branch were you assigned? Skip this question if rejected or waitlisted.
* In the preference form, which courses did you place ABOVE your allocated one?

The survey is conducted via Google Forms, which lets you export the results as a `.csv` file. The file may come zipped, in which case unzip it, and run the Python script [`cutoffs.py`](https://github.com/sidstuff/cutoffs/blob/master/cutoffs.py) in the same directory. I.e., download it to the same folder as the CSV file, open a terminal there, and run `python cutoffs.py`.
