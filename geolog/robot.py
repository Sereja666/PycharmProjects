import os
import time

from flask import Flask, render_template, request, flash, redirect
import pandas as pd

# df_all = pd.read_excel('Приложение Ж.xlsx', sheet_name='Белая', header=[0, 1, 2])
# df_footer = df_all.tail(8)
# df_top = df_all.drop(df_all.tail(8).index, axis=0,inplace=True) # drop last n rows

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'my_pdf_tools', 'png', 'jpg', 'jpeg', 'gif'}



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/choice', methods=['GET', 'POST'], endpoint='get_response') #
def upload_file():
    if request.method == 'POST':
    # проверим, передается ли в запросе файл
        if 'file' not in request.files:
            # После перенаправления на страницу загрузки
            # покажем сообщение пользователю
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        # Если файл не выбран, то браузер может
        # отправить пустой файл без имени.
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'temp.xlsx'))
            time.sleep(3)
            try:
                df_all = pd.read_excel('uploads/temp.xlsx', sheet_name='Белая', header=[0, 1, 2])
                df_footer = df_all.tail(8)
                df_all.drop(df_all.tail(8).index, axis=0, inplace=True)  # drop last n rows
                df_all['Содержание частиц, %'] = df_all['Содержание частиц, %'].fillna(0)

                for index, value in df_all.iterrows():

                    df_all.loc[index, 'это 100?'] = value['Содержание частиц, %'].sum(axis=0)
                # df_all['это 100?'] = df_all['это 100?'].astype(int)


                print(df_all.to_string())
            except Exception:
                return '''
    <!doctype html>
    <title>гавно</title>
    <h1>какое-то гавно с файлом</h1>
  
    '''
            return render_template('htmltest.html', df = df_all, df_footer=df_footer)
    return render_template('htmltest.html')

@app.route("/", methods=['GET'])
def start_page():
    return render_template('htmltest.html')

@app.route("/choice", methods=['GET'])
def choice():
    return render_template('htmltest.html')


if __name__ == '__main__':
    app.run(debug=True)