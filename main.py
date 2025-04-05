import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters"""
    return weight / (height ** 2)

def bmi_category(bmi):
    """Return BMI category based on BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Set page config
    st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")
    
    # Title and description
    # Title and description
    st.title("BMI Calculator by Owais Qazi")
    st.markdown("#Student of Generative AI and AI Agentic (GIAIC - Q3)")
    st.markdown("##Calculate your Body Mass Index (BMI)")
    st.write("""
    Body Mass Index (BMI) is a person's weight in kilograms divided by the square of height in meters. 
    A high BMI can indicate high body fatness.
    """)
    
    # Create two columns for input
    col1, col2 = st.columns(2)
    
    with col1:
        # Weight input
        weight_unit = st.radio("Weight unit:", ("kg", "lbs"))
        weight = st.number_input(f"Enter your weight ({weight_unit}):", min_value=0.0, value=70.0, step=0.1)
        
    with col2:
        # Height input
        height_unit = st.radio("Height unit:", ("cm", "meters", "feet"))
        height = st.number_input(f"Enter your height ({height_unit}):", min_value=0.0, value=1.75, step=0.01)
    
    # Convert units if necessary
    if weight_unit == "lbs":
        weight = weight * 0.453592  # Convert lbs to kg
    
    if height_unit == "cm":
        height = height / 100  # Convert cm to meters
    elif height_unit == "feet":
        height = height * 0.3048  # Convert feet to meters
    
    # Calculate BMI when button is clicked
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        # Display results
        st.success(f"Your BMI is: **{bmi:.1f}**")
        st.info(f"Category: **{category}**")
        
        # Show BMI chart for reference
        st.subheader("BMI Categories:")
        st.write("- Underweight: BMI < 18.5")
        st.write("- Normal weight: 18.5 ≤ BMI < 25")
        st.write("- Overweight: 25 ≤ BMI < 30")
        st.write("- Obese: BMI ≥ 30")
        
        # Visual indicator
        st.progress(min(bmi / 40, 1.0))  # Cap at 40 BMI for visualization

if __name__ == "__main__":
    main()