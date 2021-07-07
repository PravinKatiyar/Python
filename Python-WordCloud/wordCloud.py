from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
counts_dict = dict()
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    for word in uninteresting_words:
        file_contents=file_contents.replace(' ' + word + ' ', ' ')
    #print (file_contents)
    
    for word in punctuations:
        file_contents=file_contents.replace(word,' ')
   # print(file_contents)
    
    str=file_contents
    
    words = str.split()

    for word in words:
        if word in counts_dict:
            counts_dict[word] += 1
        else:
            counts_dict[word] = 1
    return counts_dict

  
print(calculate_frequencies("Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve.,All our dreams can come true, if we have the courage to pursue them."))

wordcloud = WordCloud(background_color='white',
                      width=1500,
                      height=1000
                      ).generate_from_frequencies(counts_dict)
# use .generate(space_separated_string) - to generate cloud from text

plt.figure(figsize=(9,6))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
