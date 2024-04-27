#!/usr/bin/env python
# coding: utf-8

# In[1]:


import flet as ft
import numpy as np
import time


# In[95]:


def main(page: ft.Page):
    # 排版
    page.title = "Game"
    page.window_width = 1200
    page.window_height = 800
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    blank = ft.Text(" ", size=20)
    title_size = 80
    bn_size = 40
    screen_height = 700
    mode = ' '
    
    # 回報模式
    def pvp_mode(e):
        global mode, mode_text
        mode = 'pvp'
        mode_text = ft.Text("PVP Mode", size=60)
        print('PVP Mode')
        round_enter = ft.Column([
                                   ft.Container(content=ft.Column([ft.Row([round_title],
                                                                          alignment=ft.MainAxisAlignment.CENTER),
                                                                   blank,
                                                                   ft.Row([one_bn,blank,three_bn,blank,
                                                                           five_bn,blank,seven_bn,],
                                                                          spacing=50,
                                                                          alignment=ft.MainAxisAlignment.CENTER),
                                                                   blank,
                                                                   ft.Row([mode_text,back_bn],
                                                                          alignment=ft.MainAxisAlignment.SPACE_BETWEEN)],
                                                                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                                                  height=screen_height
                                               )
                            ])
        page.views.append(round_enter)
        page.update()
    def ai_mode(e):
        global mode, mode_text
        mode = 'AI'
        mode_text = ft.Text("AI Mode", size=60)
        print('AI Mode')
        round_enter = ft.Column([
                                   ft.Container(content=ft.Column([ft.Row([round_title],
                                                                          alignment=ft.MainAxisAlignment.CENTER),
                                                                   blank,
                                                                   ft.Row([one_bn,blank,three_bn,blank,
                                                                           five_bn,blank,seven_bn,],
                                                                          spacing=50,
                                                                          alignment=ft.MainAxisAlignment.CENTER),
                                                                   blank,
                                                                   ft.Row([mode_text,back_bn],
                                                                          alignment=ft.MainAxisAlignment.SPACE_BETWEEN)],
                                                                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                                                  height=screen_height
                                               )
                            ])
        page.views.append(round_enter)
        page.update()
    
    # Choose Mode Content
    title = ft.Text("Choose Mode", size=title_size)
    pvp_bn = ft.ElevatedButton(content=ft.Text(value="PVP", size=bn_size),on_click=pvp_mode)
    ai_bn = ft.ElevatedButton(content=ft.Text(value="AI", size=bn_size),on_click=ai_mode)
    # Choose Mode Page
    enter = ft.Column(controls=[title,pvp_bn,ai_bn],alignment=ft.MainAxisAlignment.SPACE_AROUND,)
#     page.add(enter)
    page.add(title)
    page.add(pvp_bn)
    page.add(ai_bn)
    page.update()
    
    # count down
    def ready():
        page.views.append(ready_text)
        page.update()
        time.sleep(1)
        page.views.append(cd3_text)
        page.update()
        time.sleep(1)
        page.views.append(cd2_text)
        page.update()
        time.sleep(1)
        page.views.append(cd1_text)
        page.update()
        time.sleep(1)
        page.views.append(go_text)
        page.update()
        time.sleep(1)
        page.views.append(ft.Column([quit_bn,]))
        page.update()
    def show_quit_bn(e):
        page.views.pop()
        page.update()
    def close(e):
#         page.window_close()
        page.views.pop()
        page.views.pop()
        page.views.pop()
        page.views.pop()
        page.views.pop()
        page.views.pop()
        page.views.pop()
        page.views.pop()
        page.update()
    # 回報局數
    def one_round(e):
        print('1 round')
        page.update()
        ready()
    def three_round(e):
        print('3 round')
        page.update()
        ready()
    def five_round(e):
        print('5 round')
        page.update()
        ready()
    def seven_round(e):
        print('7 round')
        page.update()
        ready()
    def back(e):
        print('Back')
        page.views.pop()
        page.update()
    def quit(e):
        page.views.append(quit_ask)
        page.update()
    # Choose Round Content
    round_title = ft.Text("How Many Rounds?", size=title_size)
    one_bn = ft.ElevatedButton(content=ft.Text(value="1", size=bn_size),on_click=one_round)
    three_bn = ft.ElevatedButton(content=ft.Text(value="3", size=bn_size),on_click=three_round)
    five_bn = ft.ElevatedButton(content=ft.Text(value="5", size=bn_size),on_click=five_round)
    seven_bn = ft.ElevatedButton(content=ft.Text(value="7", size=bn_size),on_click=seven_round)
    back_bn = ft.ElevatedButton(content=ft.Text(value="Back", size=bn_size),on_click=back)
#     mode_text = ft.Text(mode + " Mode", size=60)
    # the page choosing how many rounds
#     round_enter = ft.Column([
#                                    ft.Container(content=ft.Column([ft.Row([round_title],
#                                                                           alignment=ft.MainAxisAlignment.CENTER),
#                                                                    blank,
#                                                                    ft.Row([one_bn,blank,three_bn,blank,
#                                                                            five_bn,blank,seven_bn,],
#                                                                           spacing=50,
#                                                                           alignment=ft.MainAxisAlignment.CENTER),
#                                                                    blank,
#                                                                    ft.Row([mode_text,back_bn],
#                                                                           alignment=ft.MainAxisAlignment.SPACE_BETWEEN)],
#                                                                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
#                                                                   height=screen_height
#                                                )
#                             ])
    
    # countdown text
#     ready_text = ft.Column([ft.Text('READY?', size=title_size)])
    ready_text = ft.Column([
                        ft.Container(
                                      ft.Column([ft.Row([ft.Text('READY?', size=title_size)],
                                                          alignment=ft.MainAxisAlignment.CENTER)],
                                                alignment=ft.MainAxisAlignment.CENTER),
                                                height=screen_height
                                    )
                        ])
    cd3_text = ft.Column([
                        ft.Container(
                                      ft.Column([ft.Row([ft.Text('3', size=title_size)],
                                                          alignment=ft.MainAxisAlignment.CENTER)],
                                                alignment=ft.MainAxisAlignment.CENTER),
                                                height=screen_height
                                    )
                        ])
    cd2_text = ft.Column([
                        ft.Container(
                                      ft.Column([ft.Row([ft.Text('2', size=title_size)],
                                                          alignment=ft.MainAxisAlignment.CENTER)],
                                                alignment=ft.MainAxisAlignment.CENTER),
                                                height=screen_height
                                    )
                        ])
    cd1_text = ft.Column([
                        ft.Container(
                                      ft.Column([ft.Row([ft.Text('1', size=title_size)],
                                                          alignment=ft.MainAxisAlignment.CENTER)],
                                                alignment=ft.MainAxisAlignment.CENTER),
                                                height=screen_height
                                    )
                        ])
    go_text = ft.Column([
                        ft.Container(
                                      ft.Column([ft.Row([ft.Text('GO!', size=title_size)],
                                                          alignment=ft.MainAxisAlignment.CENTER)],
                                                alignment=ft.MainAxisAlignment.CENTER),
                                                height=screen_height
                                    )
                        ])
    # quit button
    quit_bn = ft.Column([
                        ft.Container(
                                      ft.Column([ft.Row([ft.ElevatedButton(content=ft.Text(value="Quit", size=bn_size),
                                                                            on_click=quit)],
                                                          alignment=ft.MainAxisAlignment.CENTER)],
                                                alignment=ft.MainAxisAlignment.CENTER),
                                                height=screen_height
                                    )
                        ])
    # quit or not
    quit_text = ft.Text('Quit?', size=title_size)
    yes_bn = ft.ElevatedButton(content=ft.Text(value="Yes", size=bn_size),on_click=close)
    no_bn = ft.ElevatedButton(content=ft.Text(value="No", size=bn_size),on_click=show_quit_bn)
#     quit_ask = ft.Column([quit_text,yes_bn,no_bn])
    quit_ask = ft.Column([
                        ft.Container(
                                      ft.Column([ft.Row([quit_text],alignment=ft.MainAxisAlignment.CENTER),
                                                ft.Row([yes_bn],alignment=ft.MainAxisAlignment.CENTER),
                                                 ft.Row([no_bn],alignment=ft.MainAxisAlignment.CENTER)],
                                                alignment=ft.MainAxisAlignment.CENTER),
                                                height=screen_height
                                    )
                        ])


# In[96]:


ft.app(target=main)


# In[ ]:




