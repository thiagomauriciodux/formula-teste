{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8c170f97-0d23-4036-8827-0907522d956a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#-- instalando libs\n",
    "#!pip install pulp\n",
    "#!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c6207f7e-bed4-4e41-920c-a5862717583c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#-- carregando as libs\n",
    "import streamlit as st\n",
    "\n",
    "from pulp import LpMaximize, LpProblem, LpStatus, LpVariable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "eac6e9f7-eb00-41fa-923a-69430548f855",
   "metadata": {},
   "outputs": [
    {
     "ename": "StreamlitAPIException",
     "evalue": "Slider value should either be an int/float/datetime or a list/tuple of 0 to 2 ints/floats/datetimes",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStreamlitAPIException\u001b[0m                     Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_16192\\3681928633.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#-- selecionando o tipo de otimização\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mproblem_optmization\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msidebar\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mslider\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Tipo Otimização\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Mínimo\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Máximo\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\streamlit\\runtime\\metrics_util.py\u001b[0m in \u001b[0;36mwrapped_func\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    309\u001b[0m                 \u001b[0m_LOGGER\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Failed to collect command telemetry\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mex\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    310\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 311\u001b[1;33m             \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnon_optional_func\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    312\u001b[0m         \u001b[1;32mfinally\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    313\u001b[0m             \u001b[1;31m# Activate tracking again if command executes without any exceptions\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\streamlit\\elements\\slider.py\u001b[0m in \u001b[0;36mslider\u001b[1;34m(self, label, min_value, max_value, value, step, format, key, help, on_change, args, kwargs, disabled, label_visibility)\u001b[0m\n\u001b[0;32m    325\u001b[0m         \"\"\"\n\u001b[0;32m    326\u001b[0m         \u001b[0mctx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mget_script_run_ctx\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 327\u001b[1;33m         return self._slider(\n\u001b[0m\u001b[0;32m    328\u001b[0m             \u001b[0mlabel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlabel\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    329\u001b[0m             \u001b[0mmin_value\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmin_value\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\streamlit\\elements\\slider.py\u001b[0m in \u001b[0;36m_slider\u001b[1;34m(self, label, min_value, max_value, value, step, format, key, help, on_change, args, kwargs, disabled, label_visibility, ctx)\u001b[0m\n\u001b[0;32m    392\u001b[0m         \u001b[0mrange_value\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtuple\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    393\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0msingle_value\u001b[0m \u001b[1;32mand\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mrange_value\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 394\u001b[1;33m             raise StreamlitAPIException(\n\u001b[0m\u001b[0;32m    395\u001b[0m                 \u001b[1;34m\"Slider value should either be an int/float/datetime or a list/tuple of \"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    396\u001b[0m                 \u001b[1;34m\"0 to 2 ints/floats/datetimes\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mStreamlitAPIException\u001b[0m: Slider value should either be an int/float/datetime or a list/tuple of 0 to 2 ints/floats/datetimes"
     ]
    }
   ],
   "source": [
    "#-- selecionando o tipo de otimização\n",
    "problem_optmization = st.sidebar.slider(\"Tipo Otimização\", \"Mínimo\", \"Máximo\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e1e5b5b-3989-4426-818c-816f5cf7a9e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the maximization problem\n",
    "if problem_optmization == 'Máximo\":\n",
    "    model = LpProblem(name='Field Problem', sense=LpMaximize)\n",
    "    \n",
    "    # Initialize the variables\n",
    "    x = LpVariable(name=\"x\", lowBound=0, upBound=100)\n",
    "    y = LpVariable(name=\"y\", lowBound=0, upBound=100)\n",
    "    \n",
    "    # Add the constraints to the model. Use += to append expressions to the model\n",
    "    model += (x <= 95, \"margin_X\") #it cannot go past the fence\n",
    "    model += (y <= 95, \"margin_Y\")\n",
    "    \n",
    "    # Objective Function\n",
    "    obj_func = x + y\n",
    "    # Add Objective function to the model\n",
    "    model += obj_func\n",
    "    \n",
    "    status = model.solve()\n",
    "    \n",
    "    print(status)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
