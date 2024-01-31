import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import de la base voiture
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voiture = pd.read_csv(link)

# Copie du dataframe sans colone 'continent'
df_voiture_num = df_voiture.select_dtypes(include='number')

# Copie du dataframe part continent et avec suppression de la colonne 'continent'
df_voiture_us = df_voiture_num[df_voiture['continent'] == ' US.']
df_voiture_europe = df_voiture_num[df_voiture['continent'] == ' Europe.']
df_voiture_japan = df_voiture_num[df_voiture['continent'] == ' Japan.']

st.title("EVOLUTION DE l'AUTOMOBILE DEPUIS 1970")

st.write('ANALYSE PAR CONTINENTS ( US - EUROPE - JAPON )')

# Creation d'une fonction pour generer les graph par continent
def plot_voiture(selected_data):
    if selected_data == 'US':
        st.write('Voici les resultats pour les US')
        
        # premieère ligne de graph
        fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.lineplot(x=df_voiture_us['year'], y=df_voiture_us['hp'], ax=ax1)
        ax1.set_xlabel('Annee')
        ax1.set_ylabel('Puissance (hp)')
        ax1.set_title('EVOLUTION DE LA PUISSANCE')
        
        sns.lineplot(x=df_voiture_us['year'], y=df_voiture_us['cylinders'], ax=ax2)
        ax2.set_xlabel('Annee')
        ax2.set_ylabel('Cylindres')
        ax2.set_title('EVOLUTION DU NOMBRE DE CYLINDRES')
        
        plt.tight_layout()
        st.pyplot(fig1)
        st.write('Sur ces courbes, nous remarquons que la puissance semble diminuer en même temps que le nombre de cylindres. Nous remarquons principalement le phénomène en 1972 et 1981')

        # deuxièmee ligne de graph
        fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.lineplot(x=df_voiture_us['year'], y=df_voiture_us['cubicinches'], ax=ax1)
        ax1.set_xlabel('Annees')
        ax1.set_ylabel('volume (inches*3)')
        ax1.set_title('EVOLUTION DU VOLUME')
                               
        sns.lineplot(x=df_voiture_us['year'], y=df_voiture_us['weightlbs'], ax=ax2)
        ax2.set_xlabel('Annees')
        ax2.set_ylabel('Poids en (pound)')
        ax2.set_title('EVOLUTION DU POIDS')
        
        plt.tight_layout()
        st.pyplot(fig2)
        st.write("De même le poids et le volume des véhicules n'ont céssé de diminuer depuis 1974.") 

        # troisième ligne de graph
        fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.lineplot(x=df_voiture_us['year'], y=df_voiture_us['time-to-60'], ax=ax1)
        ax1.set_xlabel('Annees')
        ax1.set_ylabel('temps au 60 mph')
        ax1.set_title("EVOLUTION DE L'ACCELERATION")
        
        sns.lineplot(x=df_voiture_us['year'], y=df_voiture_us['mpg'], ax=ax2)
        ax2.set_xlabel('Annees')
        ax2.set_ylabel('Consommation (miles per gallon)')
        ax2.set_title("EVOLUTION DE LA CONSOMMATION")
        
        plt.tight_layout()
        st.pyplot(fig3)
        st.write('Cette fois nous remarquons que la consommation et la puissance des véhicules augmentent inversement au poids, a la puissance et au nombre de cylinde. Nous pouvons suposer que cela est du a la modernisation des moteurs.')

        # quatrième ligne de graph
        fig4, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.histplot(df_voiture_us['hp'], bins=20, kde=True, ax=ax1)
        ax1.set_xlabel('Horsepower (hp)')
        ax1.set_ylabel('Frequency / Density')
        ax1.set_title('DISTRIBUTION DE LA PUISSANCE')
        
        viz_correlation = sns.heatmap(df_voiture_us.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True), ax=ax2)
        ax2.set_title('Schema de correlation')

        st.pyplot(fig4)
        st.write('La courbe de distribution nous montre que les US ont produis en majorité des moteurs de 80 et 150 chevaux.')
        st.write('Enfin le graphique de corrélations nous montre la forte corrélation négative entre la consommation et le groupe - puissance, volume, poids, cylindres -.')
        st.write('\nDATASET US COMPLET :')
        df_voiture_us


    elif selected_data == 'EUROPE':
        st.write("Voici les resultats pour l'EUROPE")
        
        # premieère ligne de graph
        fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.lineplot(x=df_voiture_europe['year'], y=df_voiture_europe['hp'], ax=ax1)
        ax1.set_xlabel('Annee')
        ax1.set_ylabel('Puissance (hp)')
        ax1.set_title('EVOLUTION DE LA PUISSANCE')
        
        sns.lineplot(x=df_voiture_europe['year'], y=df_voiture_europe['cylinders'], ax=ax2)
        ax2.set_xlabel('Annee')
        ax2.set_ylabel('Cylindres')
        ax2.set_title('EVOLUTION DU NOMBRE DE CYLINDRES')
        
        plt.tight_layout()
        st.pyplot(fig1)
        st.write('Ici nous remarquons une faible évolution des cylindrées en Europe mais une tendance a la baisse cylindrée/puissance depuis 1980')

        # deuxièmee ligne de graph
        fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.lineplot(x=df_voiture_europe['year'], y=df_voiture_europe['cubicinches'], ax=ax1)
        ax1.set_xlabel('Annees')
        ax1.set_ylabel('volume (inches*3)')
        ax1.set_title('EVOLUTION DU VOLUME')
                               
        sns.lineplot(x=df_voiture_europe['year'], y=df_voiture_europe['weightlbs'], ax=ax2)
        ax2.set_xlabel('Annees')
        ax2.set_ylabel('Poids en (pound)')
        ax2.set_title('EVOLUTION DU POIDS')
        
        plt.tight_layout()
        st.pyplot(fig2)
        st.write("Encore une fois nous remarquons une constance dans le volume (115) et le poids (2400) des véhicules Européens.") 

        # troisième ligne de graph
        fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.lineplot(x=df_voiture_europe['year'], y=df_voiture_europe['time-to-60'], ax=ax1)
        ax1.set_xlabel('Annees')
        ax1.set_ylabel('temps au 60 mph')
        ax1.set_title("EVOLUTION DE L'ACCELERATION")
        
        sns.lineplot(x=df_voiture_europe['year'], y=df_voiture_europe['mpg'], ax=ax2)
        ax2.set_xlabel('Annees')
        ax2.set_ylabel('Consommation (miles per gallon)')
        ax2.set_title("EVOLUTION DE LA CONSOMMATION")
        
        plt.tight_layout()
        st.pyplot(fig3)
        st.write("Phénomène équivalent aux US et JAPON, la modernisation des moteurs ont permis d'augmenter l'accélération au dépend de la consommation.")

        # quatrième ligne de graph
        fig4, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.histplot(df_voiture_europe['hp'], bins=20, kde=True, ax=ax1)
        ax1.set_xlabel('Horsepower (hp)')
        ax1.set_ylabel('Frequency / Density')
        ax1.set_title('DISTRIBUTION DE LA PUISSANCE')
        
        viz_correlation = sns.heatmap(df_voiture_europe.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True), ax=ax2)
        ax2.set_title('Schema de correlation')

        st.pyplot(fig4)
        st.write('La courbe de distribution nous montre que les US ont produis en majorité des moteurs de 40 chevaux et entre 70 et 115 chevaux.')
        st.write('Enfin le graphique de corrélations nous montre la forte corrélation négative entre la consommation et le groupe - puissance, volume, poids, cylindres -.')
        st.write('\nDATASET EUROPE COMPLET :')
        df_voiture_europe

    elif selected_data == 'JAPAN':
        st.write('Voici les resultats pour les JAPAN')
        
        # premieère ligne de graph
        fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.lineplot(x=df_voiture_japan['year'], y=df_voiture_japan['hp'], ax=ax1)
        ax1.set_xlabel('Annee')
        ax1.set_ylabel('Puissance (hp)')
        ax1.set_title('EVOLUTION DE LA PUISSANCE')
        
        sns.lineplot(x=df_voiture_japan['year'], y=df_voiture_japan['cylinders'], ax=ax2)
        ax2.set_xlabel('Annee')
        ax2.set_ylabel('Cylindres')
        ax2.set_title('EVOLUTION DU NOMBRE DE CYLINDRES')
        
        plt.tight_layout()
        st.pyplot(fig1)
        st.write('Sur ces courbes, nous remarquons que la puissance semble rester constante avec une moyenne a 80 chevaux. Nous voyons que les moteurs Japonnais ont peu évolué en cylindré')

        # deuxièmee ligne de graph
        fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.lineplot(x=df_voiture_japan['year'], y=df_voiture_japan['cubicinches'], ax=ax1)
        ax1.set_xlabel('Annees')
        ax1.set_ylabel('volume (inches*3)')
        ax1.set_title('EVOLUTION DU VOLUME')
                               
        sns.lineplot(x=df_voiture_japan['year'], y=df_voiture_japan['weightlbs'], ax=ax2)
        ax2.set_xlabel('Annees')
        ax2.set_ylabel('Poids en (pound)')
        ax2.set_title('EVOLUTION DU POIDS')
        
        plt.tight_layout()
        st.pyplot(fig2)
        st.write('Idem avec un volume moyen et un poids moyen qui évoluent peu au fil des années.')

        # troisième ligne de graph
        fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.lineplot(x=df_voiture_japan['year'], y=df_voiture_japan['time-to-60'], ax=ax1)
        ax1.set_xlabel('Annees')
        ax1.set_ylabel('temps au 60 mph')
        ax1.set_title("EVOLUTION DE L'ACCELERATION")
        
        sns.lineplot(x=df_voiture_japan['year'], y=df_voiture_japan['mpg'], ax=ax2)
        ax2.set_xlabel('Annees')
        ax2.set_ylabel('Consommation (miles per gallon)')
        ax2.set_title("EVOLUTION DE LA CONSOMMATION")
        
        plt.tight_layout()
        st.pyplot(fig3)
        st.write('Nous remarquons ici que le Japon se démarque avec une baisse de la consommation moyenne depuis 1981 en sacrifiant les besoins en accélération.')

        # quatrième ligne de graph
        fig4, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        sns.histplot(df_voiture_japan['hp'], bins=20, kde=True, ax=ax1)
        ax1.set_xlabel('Horsepower (hp)')
        ax1.set_ylabel('Frequency / Density')
        ax1.set_title('DISTRIBUTION DE LA PUISSANCE')
        
        viz_correlation = sns.heatmap(df_voiture_japan.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True), ax=ax2)
        ax2.set_title('Schema de correlation')

        st.pyplot(fig4)
        st.write('La courbe de distribution nous montre que le JAPON a produis en majorité des moteurs de 65, 70 et 95 chevaux.')
        st.write('Enfin le graphique de corrélations nous montre la corrélation négative entre la consommation et le groupe - puissance, volume, poids, cylindres -.')
        st.write('\nDATASET JAPON COMPLET :')
        df_voiture_japan


# Ajouter des boutons dans un sidebar
selected_data = st.sidebar.radio("Sélectionnez le jeu de données :", ['US', 'EUROPE','JAPAN'])

# Bouton pour générer le graphique en fonction du jeu de données sélectionné
if st.sidebar.button("Afficher le graphique"):
    plot_voiture(selected_data)

