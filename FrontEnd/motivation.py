import requests
import streamlit as st

def show_motivational_quote():
    category = 'fitness'
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    response = requests.get(api_url, headers={'X-Api-Key': 'Vt8s7q9dx5p0fLIT8gs0oA==WnHmcyW3txL8N8HE'})
    if response.status_code == 200:
        data = response.json()
        if data:
            quote_data = data[0]  # Assuming only one quote is returned
            quote = quote_data.get('quote', '')
            author = quote_data.get('author', '')
            print(quote)
            print(author)
            # Displaying the quote and author using Streamlit
            st.subheader(quote)
            st.subheader(author)
        else:
             st.error("No quotes found for the specified category.")
    else:
         st.error(f"Error: {response.status_code} - {response.text}")

# Calling the function to display the motivational quote
# show_motivational_quote()
