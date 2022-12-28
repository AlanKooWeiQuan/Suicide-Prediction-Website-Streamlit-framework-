#### Module : Statistical Analysis

## libraries
import data_loading
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def statistic_analysis (data):
    ### remove non-suicide class
    word = data.columns[1]
    for n in range(len(data)):
        if (data.loc[n,word]) == "non-suicide":
            data = data.drop(n)
    data.reset_index(drop=True, inplace=True)
    
    ### label pos, neg and neutral class for sentiment polarity     
    data["sentiment polarity class"] =""
    for n in range(len(data)):
        if data.polarity_compound.iloc[n] == 1 :
            data['sentiment polarity class'].iloc[n] = "neutral"
            continue
        elif data.polarity_compound.iloc[n] > 1 :
            data['sentiment polarity class'].iloc[n] = "positive"
        elif data.polarity_compound.iloc[n] < 1 :
            data['sentiment polarity class'].iloc[n] = "negative"
    
    ### label multiple level of pos, neg and neutral class for sentiment polarity     
    data["sentiment polarity level"] =""
    for n in range(len(data)):
        if data.polarity_compound.iloc[n] == 1 :
            data['sentiment polarity level'].iloc[n] = "neutral"
            continue
        elif data.polarity_compound.iloc[n] > 1.81 :
            data['sentiment polarity level'].iloc[n] = "very strong positive"
            continue
        elif data.polarity_compound.iloc[n] > 1.61 :
            data['sentiment polarity level'].iloc[n] = "strong positive"
            continue
        elif data.polarity_compound.iloc[n] > 1.41 :
            data['sentiment polarity level'].iloc[n] = "medium positive"
            continue
        elif data.polarity_compound.iloc[n] > 1.21 :
            data['sentiment polarity level'].iloc[n] = "weak positive"
            continue
        elif data.polarity_compound.iloc[n] > 1 :
            data['sentiment polarity level'].iloc[n] = "very weak positive"
            continue
        elif data.polarity_compound.iloc[n] > 0.81 :
            data['sentiment polarity level'].iloc[n] = "very weak negative"
            continue
        elif data.polarity_compound.iloc[n] > 0.61 :
            data['sentiment polarity level'].iloc[n] = "weak negative"
            continue
        elif data.polarity_compound.iloc[n] > 0.41 :
            data['sentiment polarity level'].iloc[n] = "medium negative"
            continue
        elif data.polarity_compound.iloc[n] > 0.21 :
            data['sentiment polarity level'].iloc[n] = "strong negative"
            continue
        elif data.polarity_compound.iloc[n] >= 0:
            data['sentiment polarity level'].iloc[n] = "very strong negative"
        else:
            data['sentiment polarity level'].iloc[n] = "PROBLEM"
    
    
    ### result of Suicide or Non-Suicide Class
    class_value = data['class'].value_counts().reset_index()
    class_value.columns = ["Suicide or Non-Suicide Class", "Frequency"]
    class_value["Percentage"] =""
    for n in range(len(class_value)):
        class_value['Percentage'].iloc[n] = class_value.loc[n,'Frequency'] / len(data)
    
    ### result of Sentiment Polarity Class
    sp_class_value = data['sentiment polarity class'].value_counts().reset_index()
    sp_class_value.columns = ["Sentiment Polarity Class", "Frequency"]
    sp_class_value["Percentage"] =""
    for n in range(len(sp_class_value)):
        sp_class_value['Percentage'].iloc[n] = sp_class_value.loc[n,'Frequency'] / len(data)
        
    ### result of Sentiment Polarity Level
    sp_level_value = data['sentiment polarity level'].value_counts().reset_index()
    sp_level_value.columns = ["Sentiment Polarity level", "Frequency"]
    sp_level_value["Percentage"] =""
    for n in range(len(sp_level_value)):
        sp_level_value['Percentage'].iloc[n] = sp_level_value.loc[n,'Frequency'] / len(data)    
        
    ### result of Emotion Class
    emotion_value = data['emotion'].value_counts().reset_index()
    emotion_value.columns = ["Emotion Class", "Frequency"]
    emotion_value["Percentage"] =""
    for n in range(len(emotion_value)):
        emotion_value['Percentage'].iloc[n] = emotion_value.loc[n,'Frequency'] / len(data)
    # print(emotion_value.loc[0,'Emotion Class'])
    # print(emotion_value.loc[0,'Frequency'])
    
    ### result of Overall
    overall = data[["class", "sentiment polarity class", "emotion"]].groupby(["class", "sentiment polarity class", "emotion"]).size().reset_index()
    overall.columns = ["class", "sentiment polarity class", "emotion", "Frequency"]
    overall["Percentage"] =""
    for n in range(len(overall)):
        overall['Percentage'].iloc[n] = overall.loc[n,'Frequency'] / len(data)
    
    ### result of Overall2
    overall_2 = data[["class", "sentiment polarity level", "emotion"]].groupby(["class", "sentiment polarity level", "emotion"]).size().reset_index()
    overall_2.columns = ["class", "sentiment polarity level", "emotion", "Frequency"]
    overall_2["Percentage"] =""
    for n in range(len(overall_2)):
        overall_2['Percentage'].iloc[n] = overall_2.loc[n,'Frequency'] / len(data)
    
    
    
    
    
    
    ### print all results
    # print("Data Size:",len(data),'\n')
    # print(class_value,'\n')
    # print(sp_class_value,'\n')
    # print(sp_level_value,'\n')
    # print(emotion_value,'\n')
    # print(overall,'\n')
    # pd.set_option('display.max_rows', None)
    # print(overall_2,'\n')
    
    ### graph (suicide vs sp class)
    # bar_pie_plot(sp_class_value)
    ### graph (suicide vs sp level)
    # bar_pie_plot(sp_level_value)
    ### graph (suicide vs emotion)
    # bar_pie_plot(emotion_value)
    
    ### graph (suicide vs overall)
    new_overall = overall.sort_values(by="Percentage", ascending=False)
    new_overall = new_overall[0:10]
    new_overall.reset_index(drop=True, inplace=True)
    # bar_pie_plot2(new_overall)
    
    ### graph (suicide vs overall2)
    new_overall1 = overall_2.sort_values(by="Percentage", ascending=False)
    new_overall1 = new_overall1[0:10]
    new_overall1.reset_index(drop=True, inplace=True)
    # bar_pie_plot2(new_overall1)

    return sp_class_value, sp_level_value, emotion_value, new_overall, new_overall1





#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
## bar_pie_plot function 1
def bar_pie_plot(data):
    if data.columns[0] == "Sentiment Polarity Class":
        colour = ['red', 'limegreen','grey']
        xlabel = 'sentiment polarity class'
        ylabel = 'number of suicide text'
        title = "Number of Suicide Text with Different Class of Sentiment Polarity"
        xtickSize = 10
        ytickSize = 10
        propSize = 10
        legendLoc = "upper right"
        xtickSize2 = 10
        ytickSize2 = 10
    elif data.columns[0] == "Sentiment Polarity level":
        colour = ["red","darkorange","gold","limegreen","mediumblue","darkviolet","deeppink","sienna","teal","cyan","pink"]
        xlabel = 'sentiment polarity level'
        ylabel = 'number of suicide text'
        title = "Number of Suicide Text with Different Level of Sentiment Polarity"
        xtickSize = 7
        ytickSize = 10
        propSize = 8
        legendLoc = "upper left"
        xtickSize2 = 10
        ytickSize2 = 10
    elif data.columns[0] == "Emotion Class":
        colour = ["red","darkorange","gold","limegreen","mediumblue","darkviolet","deeppink","sienna","teal","cyan"]
        xlabel = 'emotion class'
        ylabel = 'number of suicide text'
        title = "Number of Suicide Text with Different Emotion Class"
        xtickSize = 10
        ytickSize = 10
        propSize = 10
        legendLoc = "upper right"
        xtickSize2 = 10
        ytickSize2 = 10

    #add label function
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i]//2, y[i], ha = 'center', fontsize=14)

    ### bar plot
    # x-coordinates of left sides of bars 
    left = []
    for n in range(len(data)):
        left.append(n)
    # heights of bars
    height = []
    for n in range(len(data)):
        height.append(data.loc[n,'Frequency'])
    # labels for bars
    tick_label = []
    label_col = data.columns[0]
    for n in range(len(data)):
        tick_label.append(data.loc[n, label_col])
    # plotting a bar chart
    plt.rc('xtick', labelsize= xtickSize)    
    plt.rc('ytick', labelsize= ytickSize)
    plt.bar(left, height, tick_label = tick_label,
            width = 0.6, color = colour)
    #add label
    addlabels(tick_label, height)
    # naming the x-axis
    plt.xlabel(xlabel, fontsize=13, weight='bold')
    # naming the y-axis
    plt.ylabel(ylabel, fontsize=13, weight='bold')
    # plot title
    plt.title(title, fontsize=20, weight='bold', )
    #display value
    for index, value in enumerate(height):
        plt.text(value, index,
                 str(value))
    # function to show the plot
    st.pyplot(fig = plt, clear_figure=True)

    ### pie plot
    # plotting a pie chart
    plt.rc('xtick', labelsize= xtickSize2)    
    plt.rc('ytick', labelsize= ytickSize2)
    plt.pie(height, labels = tick_label, colors= colour, autopct = '%1.1f%%')
    # plot title
    plt.title(title, fontsize=20, weight='bold', )
    # plot legend
    plt.legend(loc=legendLoc, prop={'size': propSize})
    # function to show the plot
    st.pyplot(fig = plt, clear_figure=True)










#######################################################################################################################
#######################################################################################################################
def bar_pie_plot_1_1(data):
    colour = ['red', 'limegreen','grey']
    xlabel = 'sentiment polarity class'
    ylabel = 'number of suicide text'
    title = "Number of Suicide Text with Different Class of Sentiment Polarity"
    xtickSize = 8
    ytickSize = 8

    #add label function
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center', fontsize=10)

    ### bar plot
    # x-coordinates of left sides of bars 
    left = []
    for n in range(len(data)):
        left.append(n)
    # heights of bars
    height = []
    for n in range(len(data)):
        height.append(data.loc[n,'Frequency'])
    # labels for bars
    tick_label = []
    label_col = data.columns[0]
    for n in range(len(data)):
        tick_label.append(data.loc[n, label_col])
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(7)
    plt.rc('xtick', labelsize= xtickSize)    
    plt.rc('ytick', labelsize= ytickSize)
    plt.bar(left, height, tick_label = tick_label, width = 0.6, color = colour)
    #add label
    addlabels(tick_label, height)
    # naming the x-axis
    plt.xlabel(xlabel, fontsize=10, weight='bold')
    # naming the y-axis
    plt.ylabel(ylabel, fontsize=10, weight='bold')
    # function to show the plot
    
    st.pyplot(fig = plt, clear_figure=True)



#######################################################################################################################
def bar_pie_plot_1_2(data):
    title = "Number of Suicide Text with Different Class of Sentiment Polarity" 
    colour = ['red', 'limegreen','grey']
    propSize = 4
    legendLoc = "upper right"
    xtickSize2 = 4
    ytickSize2 = 4

    #add label function
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center', fontsize=4)

    ### bar plot
    # x-coordinates of left sides of bars 
    left = []
    for n in range(len(data)):
        left.append(n)
    # heights of bars
    height = []
    for n in range(len(data)):
        height.append(data.loc[n,'Frequency'])
    # labels for bars
    tick_label = []
    label_col = data.columns[0]
    for n in range(len(data)):
        tick_label.append(data.loc[n, label_col])
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(7)
    ### pie plot
    # plotting a pie chart
    plt.rc('xtick', labelsize= xtickSize2)    
    plt.rc('ytick', labelsize= ytickSize2)
    plt.pie(height, labels = tick_label, colors= colour, autopct = '%1.1f%%', textprops={'fontsize': 5}, radius = 0.4)
    plt.legend(loc=legendLoc, prop={'size': propSize})
    # function to show the plot
    st.pyplot(fig = plt, clear_figure=True)



#######################################################################################################################
#######################################################################################################################
def bar_pie_plot_2_1(data):
    colour = ["red","darkorange","gold","limegreen","mediumblue","darkviolet","deeppink","sienna","teal","cyan","pink"]
    xlabel = 'sentiment polarity level'
    ylabel = 'number of suicide text'
    title = "Number of Suicide Text with Different Level of Sentiment Polarity"
    xtickSize = 3
    ytickSize = 8

    #add label function
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center', fontsize=10)

    ### bar plot
    # x-coordinates of left sides of bars 
    left = []
    for n in range(len(data)):
        left.append(n)
    # heights of bars
    height = []
    for n in range(len(data)):
        height.append(data.loc[n,'Frequency'])
    # labels for bars
    tick_label = []
    label_col = data.columns[0]
    for n in range(len(data)):
        tick_label.append(data.loc[n, label_col])
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(7)
    plt.rc('xtick', labelsize= xtickSize)    
    plt.rc('ytick', labelsize= ytickSize)
    plt.bar(left, height, tick_label = tick_label, width = 0.6, color = colour)
    #add label
    addlabels(tick_label, height)
    # naming the x-axis
    plt.xlabel(xlabel, fontsize=10, weight='bold')
    # naming the y-axis
    plt.ylabel(ylabel, fontsize=10, weight='bold')
    # function to show the plot
    st.pyplot(fig = plt, clear_figure=True)



#######################################################################################################################
def bar_pie_plot_2_2(data):
    title = "Number of Suicide Text with Different Level of Sentiment Polarity"
    colour = ["red","darkorange","gold","limegreen","mediumblue","darkviolet","deeppink","sienna","teal","cyan","pink"]
    propSize = 4
    legendLoc = "upper right"
    xtickSize2 = 3
    ytickSize2 = 3

    #add label function
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center', fontsize=3)

    ### bar plot
    # x-coordinates of left sides of bars 
    left = []
    for n in range(len(data)):
        left.append(n)
    # heights of bars
    height = []
    for n in range(len(data)):
        height.append(data.loc[n,'Frequency'])
    # labels for bars
    tick_label = []
    label_col = data.columns[0]
    for n in range(len(data)):
        tick_label.append(data.loc[n, label_col])

    ### pie plot
    # plotting a pie chart
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(7)
    plt.rc('xtick', labelsize= xtickSize2)    
    plt.rc('ytick', labelsize= ytickSize2)
    plt.pie(height, labels = tick_label, colors= colour, autopct = '%1.1f%%', textprops={'fontsize': 5}, radius = 0.4)
    plt.legend(loc=legendLoc, prop={'size': propSize})
    # function to show the plot
    st.pyplot(fig = plt, clear_figure=True)



#######################################################################################################################
#######################################################################################################################
def bar_pie_plot_3_1(data):
    colour = ["red","darkorange","gold","limegreen","mediumblue","darkviolet","deeppink","sienna","teal","cyan"]
    xlabel = 'emotion class'
    ylabel = 'number of suicide text'
    title = "Number of Suicide Text with Different Emotion Class"
    xtickSize = 8
    ytickSize = 8

    #add label function
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center', fontsize=10)

    ### bar plot
    # x-coordinates of left sides of bars 
    left = []
    for n in range(len(data)):
        left.append(n)
    # heights of bars
    height = []
    for n in range(len(data)):
        height.append(data.loc[n,'Frequency'])
    # labels for bars
    tick_label = []
    label_col = data.columns[0]
    for n in range(len(data)):
        tick_label.append(data.loc[n, label_col])
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(7)
    plt.rc('xtick', labelsize= xtickSize)    
    plt.rc('ytick', labelsize= ytickSize)
    plt.bar(left, height, tick_label = tick_label, width = 0.6, color = colour)
    #add label
    addlabels(tick_label, height)
    # naming the x-axis
    plt.xlabel(xlabel, fontsize=10, weight='bold')
    # naming the y-axis
    plt.ylabel(ylabel, fontsize=10, weight='bold')
    # function to show the plot
    st.pyplot(fig = plt, clear_figure=True)



#######################################################################################################################
def bar_pie_plot_3_2(data):
    colour = ["red","darkorange","gold","limegreen","mediumblue","darkviolet","deeppink","sienna","teal","cyan"]
    title = "Number of Suicide Text with Different Emotion Class"
    propSize = 4
    legendLoc = "upper right"
    xtickSize2 = 3
    ytickSize2 = 3

    #add label function
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'upper right', fontsize=3)

    ### bar plot
    # x-coordinates of left sides of bars 
    left = []
    for n in range(len(data)):
        left.append(n)
    # heights of bars
    height = []
    for n in range(len(data)):
        height.append(data.loc[n,'Frequency'])
    # labels for bars
    tick_label = []
    label_col = data.columns[0]
    for n in range(len(data)):
        tick_label.append(data.loc[n, label_col])

    ### pie plot
    # plotting a pie chart
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(7)
    plt.rc('xtick', labelsize= xtickSize2)    
    plt.rc('ytick', labelsize= ytickSize2)
    plt.pie(height, labels = tick_label, colors= colour, autopct = '%1.1f%%', textprops={'fontsize': 5}, radius = 0.4)
    plt.legend(loc=legendLoc, prop={'size': propSize})
    # function to show the plot
    st.pyplot(fig = plt, clear_figure=True)





#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
### bar_pie_plot function 2
def bar_pie_plot2_1(data):
    col_1 = "sentiment polarity class"
    col_2 = "emotion"
    colour = ["red","darkorange","gold","limegreen","mediumblue","darkviolet","deeppink","sienna","teal","cyan"]
    xlabel = 'combination of sentiment polarity class and emotion'
    ylabel = 'number of suicide text'
    # title = "Number of Suicide Text with Different Combination of Sentiment Polarity Class and Emotion"
    xtickSize = 3
    ytickSize = 5

    
    #add label function
    def addlabels(x,y,z):
        for i in range(len(x)):
            label = str(y[i])+ '\n' + str(round((z[i]*100),2))+'%'
            plt.text(i, y[i], label, ha = 'center', va = 'bottom' ,fontsize=6)
    
    ### bar plot
    # x-coordinates of left sides of bars 
    left = []
    for n in range(len(data)):
        left.append(n)
    # heights of bars
    height = []
    for n in range(len(data)):
        height.append(data.loc[n,'Frequency']) 
    height2 = []
    for n in range(len(data)):
        height2.append(data.loc[n,'Percentage'])
    # labels for bars
    tick_label = []
    for n in range(len(data)):
        label = data.loc[n, col_1] + '\n' + data.loc[n, col_2]
        tick_label.append(label)
    # plotting a bar chart
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(7)
    plt.rc('xtick', labelsize= xtickSize)    
    plt.rc('ytick', labelsize= ytickSize)
    plt.bar(left, height, tick_label = tick_label, width = 0.8, color = colour)
    #add label
    addlabels(tick_label, height, height2)
    # naming the x-axis
    plt.xlabel(xlabel, fontsize=10, weight='bold')
    # naming the y-axis
    plt.ylabel(ylabel, fontsize=10, weight='bold')
    # plot title
    # plt.title(title, fontsize=20, weight='bold', )
    #display value
    # for index, value in enumerate(height):
    #     plt.text(value, index,
    #              str(value))
    # function to show the plot
    st.pyplot(fig = plt, clear_figure=True)

#######################################################################################################################
def bar_pie_plot2_2(data):
    col_1 = "sentiment polarity level"
    col_2 = "emotion"
    colour= ["red","darkorange","gold","limegreen","mediumblue","darkviolet","deeppink","sienna","teal","cyan"]
    xlabel = 'combination of sentiment polarity level and emotion'
    ylabel = 'number of suicide text'
    # title = "Number of Suicide Text with Different Combination of Sentiment Polarity Level and Emotion"
    xtickSize = 3
    ytickSize = 5
    
    #add label function
    def addlabels(x,y,z):
        for i in range(len(x)):
            label = str(y[i])+ '\n' + str(round((z[i]*100),2))+'%'
            plt.text(i, y[i], label, ha = 'center', va = 'bottom' ,fontsize=6)
    
    ### bar plot
    # x-coordinates of left sides of bars 
    left = []
    for n in range(len(data)):
        left.append(n)
    # heights of bars
    height = []
    for n in range(len(data)):
        height.append(data.loc[n,'Frequency']) 
    height2 = []
    for n in range(len(data)):
        height2.append(data.loc[n,'Percentage'])
    # labels for bars
    tick_label = []
    for n in range(len(data)):
        label = data.loc[n, col_1] + '\n' + data.loc[n, col_2]
        tick_label.append(label)
    # plotting a bar chart
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(7)
    plt.rc('xtick', labelsize= xtickSize)    
    plt.rc('ytick', labelsize= ytickSize)
    plt.bar(left, height, tick_label = tick_label, width = 0.8, color = colour)
    #add label
    addlabels(tick_label, height, height2)
    # naming the x-axis
    plt.xlabel(xlabel, fontsize=10, weight='bold')
    # naming the y-axis
    plt.ylabel(ylabel, fontsize=10, weight='bold')
    # plot title
    # plt.title(title, fontsize=20, weight='bold', )
    #display value
    # for index, value in enumerate(height):
    #     plt.text(value, index,
    #              str(value))
    # function to show the plot
    st.pyplot(fig = plt, clear_figure=True)
