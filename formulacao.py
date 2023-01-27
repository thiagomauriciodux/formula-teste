#-- carregando as libs
import streamlit as st
from pulp import LpMaximize, LpProblem, LpStatus, LpVariable

#-- títulos
st.title ("App de Formulação")
st.header("Formulação")

#-- selecionando o tipo de otimização
tipos_opt = ["Selecione", "Máxima","Mínimo"]
choice = st.sidebar.selectbox("Selecione a Otimização",tipos_opt)

#-- inputs
x = st.number_input('Escolha um valor', 0,10)
sinal = st.selectbox('Esse número deve ser',['Menor ou igual', 'Menor', 'Igual', 'Maior ou igual', 'Maior'])

#-- criando a otimização
if choice == "Máxima":
    model = LpProblem(name='Field Problem', sense=LpMaximize)
    
    #-- inicializando as variáveis
    #x = LpVariable(name="x", lowBound=0, upBound=100)
    y = LpVariable(name="y", lowBound=0, upBound=100)
    
    if sinal == 'Maior ou igual':
        #-- adicionando as restrições. Use += para apendas as expressões ao modelo
        model += (x <= 95, "margin_X")
        model += (y <= 95, "margin_Y")
    
        #-- função objetiva
        obj_func = x + y
        #-- adicionando a função objetiva ao modelo
        model += obj_func
    
        status = model.solve()
        
        #-- printando o resultado
        new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 42px;">{status}</p>'
        st.markdown(new_title, unsafe_allow_html=True)
    
    else:
        status = "Não aprendi ainda"
        new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 42px;">{status}</p>'
        st.markdown(new_title, unsafe_allow_html=True)