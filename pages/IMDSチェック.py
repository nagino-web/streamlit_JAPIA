import streamlit as st
from auth import require_login

@require_login
def contents():

    code = '''
    import streamlit as st
    st.title('asdfa')
    '''

    st.code(code, language='python')

if __name__ == "__main__":
    contents()
