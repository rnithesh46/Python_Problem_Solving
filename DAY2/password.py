import streamlit as st
st.title("Password Validation and Encryption")
password=st.text_input("Enter the password: ",type="password")
if st.button("Validate and Encrypt"):
    if password=="":
        st.error("Please enter a password.")
    elif len(password)<8:
        st.error("Password should be at least 8 characters long.")
    elif password[4] not in '12345':
        st.error("5th character should be a digit between 1 and 5.")
    elif not password.isalnum():
        st.error("Password is not alphanumeric.")
    else:
        has_uppercase=any(i.isupper() for i in password)
        has_lowercase=any(i.islower() for i in password)
        if not has_uppercase or not has_lowercase:
            st.error("Password should contain at least one uppercase and one lowercase letter.")
        else:
            encrypted_password=password.replace("A","@")
            encrypted_password=encrypted_password.replace("b","1")
            encrypted_password=encrypted_password.replace("a","B")
            # encrypted_password=password.replace("A","@").replace("b","1").replace("a","B")
            st.success("Password is valid and encrypted successfully.")
            st.write("Encrypted password is: ")
            st.code(encrypted_password)