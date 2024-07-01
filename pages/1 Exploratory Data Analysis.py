import streamlit as st

# set title
st.title("Exploratory Data Analysis")

# part 1 website time
with st.expander("1. Daily time spent on Internet"):
    st.markdown("""
#### Engagement Level:
- **Higher Engagement:** Users who click on ads tend to spend more time on the website. This indicates that higher engagement with the site correlates with a higher likelihood of ad interaction. These users are possibly finding the content more relevant or engaging, leading to longer site visits and a greater chance of interacting with ads.
- **Lower Engagement:** Users who do not click on ads spend less time on the site, suggesting that they may not find the content as engaging or relevant. This lower engagement level could result in fewer ad clicks.
""")
    st.image("./pictures/1.png", caption="Daily time spent on site Distribution", width=400, clamp=True)
    st.markdown("""
#### Internet Usage Behavior:
- **Ad Clickers:** The fact that users who click on ads have lower daily internet usage might suggest that these users are more selective or focused in their online activities. They might be more deliberate in their actions, including clicking on ads that are relevant or interesting to them.
- **Non-Ad Clickers:** Higher daily internet usage among non-ad clickers could indicate that these users are browsing more broadly and may be less focused on specific content or ads. This broader usage could dilute their attention and reduce the likelihood of clicking on ads.
""")
    st.image("./pictures/2.png", caption="Daily Internet Usage Distribution",  width=400, clamp=True)
    st.markdown("""
#### Implications for Advertisers:
- **Targeting Strategies:** Advertisers could use this data to refine their targeting strategies. For example, they might focus on users with lower daily internet usage who are more likely to click on ads, as these users may be more engaged and receptive to ad content.
- **Ad Placement:** Advertisers could also consider ad placement and design to attract users with higher daily internet usage. By creating more engaging and relevant ad content, they may be able to capture the attention of these users and increase ad interaction.
""")    
    
        


# part 2 age
with st.expander("2. Age Distribution"):
    st.markdown("""
#### Age Distribution of Website Visitors:
- The majority of the website visitors are in the age range of 31-40 years, followed by younger adults aged 21-30, and then older adults aged 41-50.
- Totally, the middle-aged group makes up the largest proportion of website visitors.
             """)
    st.image("./pictures/22.png",  width=400, clamp=True)
    st.markdown("""
#### Ad Click Analysis by Age Group:  
- **41-50 Years Old:** This age group has the highest ad click rate. This suggests that older adults are more likely to engage with ads on the site. They might find the ads more relevant or compelling, or they might have more disposable income to make purchases.
- **31-40 Years Old:** This group, while being the largest browsing demographic, also has a significant number of ad clicks. However, they are also the most common group for non-ad clicks, indicating a varied engagement with ads.
- **21-30 Years Old:** This younger group is less likely to click on ads compared to older groups. They might be more selective or skeptical about ads, or they might use ad blockers more frequently.
#### Targeted Ad Campaigns:
- **21-30 Age Group:** Focus on creating engaging, authentic, and interactive ad content. Consider using influencers or social proof to build trust and encourage ad clicks.
- **31-40 Age Group:** Since this group is large and has varied engagement with ads, employ A/B testing to determine the most effective ad formats and content. Personalize ads to cater to the diverse interests within this age group.
- **41-50 Age Group:** Keep the current advertising model, or make small enhancements.
""")
    st.image("./pictures/3.png",  width=600, clamp=True)
    
   
# part 3 gender
with st.expander("3. Gender Discount"):
    st.markdown("""
The gender distribution of viewers to the website is relatively balanced, with slightly more women than men.      
""")
    st.image("./pictures/23.png", caption="Gender Distribution for all views", width=350, clamp=True)
    st.markdown("""
- Female click on adverts slightly more often than they don't, while the opposite is true for male. However, the difference in the percentage of whether or not they clicked was not very large.
- Overall, the content of the adverts may be more appealing to **females**; whereas males may be more wary of the content of the adverts or more selective about the content of the adverts.      
""")
    st.image("./pictures/8.png", width=600, clamp=True)
   
    
# part 4 Area Income Distribution
with st.expander("4. Income Distribution"):
    st.markdown("""
**Those who click on the ads are more skewed towards people in lower income areas, while those who don't are more skewed towards higher income people.**
- This may be because low-income people are more sensitive to adverts, or they are more likely to be attracted to them. Higher-income people may be 
                more cautious or more selective about advertising content.
- The current design and positioning of advertisement content may be more orientated towards value for money rather than high quality,
                and therefore more appealing to lower income groups. This should be further analysed depending on the ad content and product positioning.
- It is recommended that advert content and positioning be adjusted to better appeal to higher income groups. Consideration could be 
                given to improving the quality and uniqueness of the adverts, or targeting them to the needs of high-income groups.
""")
    st.image("./pictures/4.png",caption='Area Income distribution',width=400, clamp=True)
    
    
# part 5 Location
with st.expander("5. Location Distribution"):
    st.markdown("""
#### High Density Regions:
The most intense regions (red areas) are located in:
- North America, particularly the eastern and central parts.
- Western Europe.
- Central Africa.
- Parts of South Asia.
- Northern South America.
""")
    st.image("./pictures/5.png",caption='Heatmap of Location Distribution',use_column_width=True)
    st.markdown("""
#### Targeted Advertising:
- For marketing or advertising purposes, focusing efforts on the red and yellow regions could yield higher engagement due 
                to the higher concentration of users.
- Tailoring content to the demographics and preferences of these high-density regions can improve the effectiveness of ad campaigns.
                
""")
    
    st.markdown("""
#### The graph shows top 10 countries with highest clicks on ads.
- **Accurate advertising:** By identifying the countries with the highest click-through rates, companies can target their advertising 
                resources more accurately, increasing the effectiveness of their adverts and improving conversion rates.
- **Market Expansion Strategy:** These countries may become important targets for future market expansion, allowing companies to develop 
                more targeted market entry strategies.          
""")
    
    st.image("./pictures/6.png",use_column_width=True)
    st.markdown("""
#### The graph shows the countries with no clicks on ads.
By identifying countries with no clicks, companies can analyze the reasons behind the lack of engagement and improve the advertising content,
                or give up the market in these countries directly to control the cost of advertising.
""")
    st.image("./pictures/7.png",caption='countries with no clicks',use_column_width=True)
    

# part 6 peak time click ads
with st.expander("6. Peak Time Click Ads"):
    st.markdown("""
#### Peak Time Analysis:
As you can see from the chart above, **Sunday** is the peak time of the week; **April** is the peak time of the year; and **9pm** is the peak time of the day.
#### Implications for Advertisers:
- Advertisements can be increased during periods of high click-through rates to increase exposure and click-through rates.
- Higher click-through rates in certain months may reflect seasonal trends. For example, months with high click-through rates 
                may be due to significant holidays or shopping seasons in those months. Plan special marketing campaigns, 
                such as holiday promotions and end-of-season clearance, during months with peak click-through rates to attract 
                more users to click on the ads.
""")
    st.image("./pictures/9.png",width=600, clamp=True)
    st.image("./pictures/10.png",width=600, clamp=True)
    st.image("./pictures/11.png",width=600, clamp=True)
    

# part 7 Ad Topic Line
with st.expander("7. Ad Topic"):
    st.markdown("""
#### The chart lists the top 10 most clicked ad topics
- These Ads be analyzed for content and creativity to identify **commonalities**. For example, whether there is a specific theme, design style or copy that can attract users to click.
- The **audience characteristics** of these ads, such as age, gender, interests, etc., can be further analysed to assess the audience matching degree, 
                and the **channels** (e.g. social media, search engines, video platforms, etc.) where these ads are mainly placed can also be analysed 
                to find out the channels with the best results.                
""")
    st.image("./pictures/12.png",use_column_width=True)
    st.markdown("""             
#### The chart lists the 10 adverts with a relatively high number of views among those with 0 clicks;
- **Content problem:** Although these adverts attracted a large number of views, they were not clicked, probably because the content was not attractive enough for users to click. The content of the advertisement needs to be analysed to see if it does not match the user's interests and needs.
- **Click inducement:** Evaluate whether the adverts lack a clear call to action (CTA, Call to Action), such as "Click to learn more", "Buy now" and so on.
- **Target Audience:** Check whether these adverts are accurately targeted to uninterested or irrelevant groups of users.           
""")
    st.image("./pictures/24.png",use_column_width=True)
    
    
