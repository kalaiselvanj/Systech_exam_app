from django.urls import path,re_path
from . import views
from . import webcam_socket

urlpatterns = [
    # path('',views.sidebar,name='base'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('candidate_dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
    path('jobposition/', views.job_positions, name='jobposition'),
    path('jobposition/add_new_job_positions/', views.add_new_job_positions, name='add_new_job_positions'),
    path('delete_job_pos/<int:id>', views.delete_job_pos, name='delete_job_pos'),
    path('edit_job_pos/<int:id>', views.edit_job_pos, name='edit_job_pos'),
    path('activatePosition/<int:id>', views.activatePosition, name='activatePosition'),
    path('subject/', views.subject, name='subject'),
    path('delete_subject/<int:id>', views.delete_subject, name='delete_subject'),
    path('edit_subject/<int:id>/', views.edit_subject, name='edit_subject'),
    path('activateSubject/<int:id>', views.activateSubject, name='activateSubject'),
    path('subject/new_subject/', views.new_subject, name='new_subject'),
    path('skill_set_config/', views.skill_set_config, name='skill_set_config'),
    path('edit_skill/<int:id>', views.edit_skill, name='edit_skill'),
    path('delete_skill/<int:id>', views.delete_skill, name='delete_skill'),
    path('activate_skill/<int:id>', views.activate_skill, name='activate_skill'),
    path('skill_set_config/create_Skill/', views.create_Skill, name='create_Skill'),
    path('quest_bank/', views.quest_bank, name='quest_bank'),
    path('quest_bank/add_quest/', views.add_quest, name='add_quest'),
    path('edit_ques/<int:id>', views.edit_ques, name='edit_ques'),
    path('delete_ques/<int:id>', views.delete_ques, name='delete_ques'),
    path('activate_quest/<int:id>', views.activate_quest, name='activate_quest'),
    path('result/', views.result, name='result'),
    path('registration/', views.registration, name='registration'),
    re_path(r'^/(?P<stream_path>(.*?))/$',views.dynamic_stream,name="videostream"),  
    path('exam_portal',views.exam_portal,name="index"),
    path('exam_main_dashboard',views.exam_main_dashboard,name="exam_main_dashboard"),
    path('alertpage',views.alertpage,name="alertpage"),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('submission/', views.submission, name='submission'),
    path('submit_answers/', views.submit_answers, name='submit_answers'),
    path('save_image/', views.save_image, name='save_image'),
    path('capture/', views.capture, name='capture'),
    path('capture_card/', views.capture_card, name='capture_card'),
    path('image_view/', views.image_view, name='image_view'),
    path('generate-excel/', views.generate_excel, name='generate_excel'),
    path('show_candidate_data/<int:id>', views.show_candidate_data, name='show_candidate_data'),
    path('registercandidate/',views.registercandidate,name='registercandidate'),
    path('video/',views.camera_part,name='video'),
    # path('live_feed/', views.live_feed, name='live_feed'),
    path('detect_face/', views.detect_face, name='detect_face'),
    
]


websocket_urlpatterns = [
    re_path(r'ws/$', webcam_socket.WebcamConsumer.as_asgi()),
]
