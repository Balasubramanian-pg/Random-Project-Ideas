
# How much are the most popular data analyst skills paid for?

Luke Barousse has collected a great (and real-time updated) dataset of Data Analyst job postings. He has also performed an extensive analysis and I wanted to add a little to it. I want to explore not only the popularity of certain analytics skills, but also what salary is expected to be offered to their lucky owners.

First and foremost, let's see what our data looks like (+ a couple of tweaks to prettify the data).

# Data Pin Point
Now to what we're interested in:
Step 1. Define Top 10 most popular (most frequently occurring) skills.
Step 2. Compute average yearly salaries for job postings that require those skills.

## Preparing for Visualization


This data can be visualised with a treemap where:

    area is responsible for the popularity of a skill (number of jobs that require the skill);
    color saturation shows the salary range.


# Takeaways

    The most popular skill is SQL (2375 postings) with an average salary of $104,468, which is close to the median value.
    The second-popular skill is Excel (1668 postings). However, the average pay for it is way lower: $94,816.
    The highest paid skill is Snowflake with an average salary of $111,506.
    Nevertheless, the demand is quite low (383 postings).
    Microsoft Word is the least common (317 postings) and also the lowest paid ($84,841).
    The "sweet spot" skill is R. It combines the second-highest average salary ($108,398) with a moderate demand (1001 postings).

