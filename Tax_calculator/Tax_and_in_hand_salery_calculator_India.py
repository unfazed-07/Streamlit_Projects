import streamlit as st
#Finding Income Tax(including CESS)
def calculate_tax(taxable_income):
    slabs=[
        (300000, 0),
        (600000, 0.05),
        (900000, 0.1),
        (1200000, 0.15),
        (1500000, 0.2),
        (float('inf'), 0.3)
    ]

    prev_slab=0
    tax=0

    for limit, rate in slabs:
        if taxable_income>limit:
            tax+=(limit-prev_slab)*rate
            prev_slab=limit
        else:
            tax+=(taxable_income-prev_slab)*rate
            break
    cess = tax * 0.04
    return tax + cess

#Finding epf deduction
def epf_deduction(CTC):
    base_sal=0.4*CTC
    epf=.12*base_sal
    return epf 

# Main Function
def take_home_salery(CTC):
    standard_deducation=50000
    professional_tax=2500 #2500 is considered for professional tax, though it vaies by states, i have taken its avergae or rough estimate
    taxable_income=CTC-standard_deducation
    income_tax=calculate_tax(taxable_income)
    epf_ded=epf_deduction(CTC)
    net_salery=CTC  -  income_tax  -  epf_ded  -  professional_tax
    return {
        "CTC": f"₹{CTC}",
        "\nTaxable Income":f"₹{taxable_income}",
        "Income Tax(Including Cess)":f"₹{income_tax}",
        "EPF deduction":f"₹{epf_ded}",
        "Professional Tax":f"₹{professional_tax:.2f} (estimated)",
        "\nNet Take-Home(Yearly)":f"₹{round(net_salery,2)}",
        "Net Take-Home(Monthly)":f"₹{round(net_salery/12,2)}"
    }
#Provide inputs and get 
with st.container(border=True):
    st.title("Tax and In-Hand Salary Estimator")
    salary = st.number_input("Enter your Annual CTC (₹):", min_value=0.0, step=1000.0)
    if st.button("View Breakdown"):
        if salary > 0:
            result = take_home_salery(salary)
            with st.container(border=True):
                st.subheader("Salery Breakdown")
                for key, value in result.items():
                    st.write(f"{key}: {value}")
        else:
            st.warning("Please enter a valid Annual CTC amount.")
