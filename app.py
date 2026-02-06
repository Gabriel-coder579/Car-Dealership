import streamlit as st
import time

# Style and set up
st.set_page_config(page_title="Exotic Cars Dealership", page_icon="🚗")

# Streamlit reruns the whole script on every click. 
# We use 'session_state' to remember if the user is logged in or what car they picked.
if 'step' not in st.session_state:
    st.session_state.step = "registration" # Start at registration
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""


def register():
    st.title("Welcome to Exotic Cars 🏎️")
    # st.text_input replaces the terminal's input()
    name = st.text_input("Enter your name:").upper().strip()
    
    # st.button returns True ONLY when clicked
    if st.button("Register"):
        if name.isalpha():
            # st.spinner shows a loading icon (replaces manual time.sleep printouts)
            with st.spinner("Processing registration..."):
                time.sleep(2)
            st.session_state.user_name = name
            st.session_state.step = "showroom"
            st.rerun() # Tells Streamlit to refresh the page immediately
        else:
            st.error("Please enter a valid name (letters only).")

def show_cars():
    st.title(f"Hello {st.session_state.user_name}, I'm Angel")
    st.subheader("Our 2026 Collection")
    
    # Dictionary mapping car names to [Price, Image URL]
    cars = {
        "Porsche Cayenne 2026": [250000, "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&q=80&w=800"],
        "Audi RS 7 2026": [200000, "https://images.unsplash.com/photo-1606152421802-db97b9c7a11b?auto=format&fit=crop&q=80&w=800"],
        "Mercedes Benz GLE Coupe AMG 2026": [150000, "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?auto=format&fit=crop&q=80&w=800"],
        "Mercedes Benz E63 AMG 2026": [190000, "https://images.unsplash.com/photo-1622199024103-60589a194916?auto=format&fit=crop&q=80&w=800"]
    }
    
    # Creating the dropdown
    selected = st.selectbox("Which car caught your eye?", list(cars.keys()))
    
    #UI Layout Elements
    # st.columns(2) splits the screen into two halves
    col1, col2 = st.columns(2)
    
    with col1:
        # Displaying the image of the selected car
        st.image(cars[selected][1], caption=selected, use_container_width=True)
        
    with col2:
        # Displaying details and price
        st.write("### Specifications")
        st.write("- **Year:** 2026")
        st.write(f"- **Price:** ${cars[selected][0]:,}")
        st.write("- **Availability:** In Stock")
        
        if st.button("Proceed to Payment"):
            st.session_state.selected_car = selected
            st.session_state.price = cars[selected][0]
            st.session_state.step = "payment"
            st.rerun()

def payment():
    st.title("Secure Checkout 💳")
    st.write(f"Car: **{st.session_state.selected_car}**")
    st.write(f"Total: **${st.session_state.price:,}**")
    
    method = st.radio("How would you like to pay?", ["Online", "In-Person"])
    
    if method == "Online":
        card = st.text_input("Enter Card Number", type="password") # Hiding the text!
        if st.button("Complete Purchase"):
            if card.isdigit() and len(card) >= 10:
                with st.spinner("Authorizing..."):
                    time.sleep(3)
                st.balloons() # Celebratory animation!
                st.success("Congratulations! Your car is ready for pickup.")
            else:
                st.error("Invalid card number.")
    else:
        st.info("Please visit our showroom at 8 Watling Merrick Park to finish your purchase.")


# Deciding which "screen" to show based on the session state
if st.session_state.step == "registration":
    register()
elif st.session_state.step == "showroom":
    show_cars()
elif st.session_state.step == "payment":

    payment()

