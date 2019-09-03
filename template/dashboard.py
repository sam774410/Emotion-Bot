
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,VideoSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)
# content_temp =[ SeparatorComponent(margin='md')]
# for i in ["angry","happy"]:
#     content_temp.append(BoxComponent(
#         layout = 'horizontal',
#         spacing='md',
#         contents = [
                            
#             TextComponent(text='情緒 :', size='lg', color='#9d9d9d', align='center'), 
#             TextComponent(text='{0}'.format(i), size='lg', color='#00BE00', weight='bold')
#         ]
#     ))
# [
                    




class Dashboard():
    def __init__(self):
        pass

    def show_single_result(self, imgurl, emotion, confidence):
        bubble = BubbleContainer(
            # header
            header=BoxComponent(
                layout='horizontal',
                contents=[
                    TextComponent(text='辨識結果', size='lg', color='#5b5b5b')
                ]
            ),

            #hero
            hero=ImageComponent(url='{0}'.format(imgurl), size='3xl', aspect_ratio='16:9', aspect_mode='fit'),

            # body
            body=BoxComponent(
                layout='vertical',
                spacing='md',
                contents=[SeparatorComponent(margin='md'),

                    BoxComponent(
                        layout = 'horizontal',
                        spacing='md',
                        contents = [
                            
                            TextComponent(text='情緒 :', size='lg', color='#9d9d9d', align='center'), 
                            TextComponent(text='{0}'.format(emotion), size='lg', color='#00BE00', weight='bold')
                        ]
                    ),

                    BoxComponent(
                        layout = 'horizontal',
                        spacing='md',
                        contents = [
        
                            TextComponent(text='信心值 :', size='lg', color='#9d9d9d', align='center'), 
                            TextComponent(text='{0}%'.format(confidence), size='lg', color='#00BE00', weight='bold')                                          
                        ]
                    )
                ]
            )
        )
        message = FlexSendMessage(alt_text="辨識結果", contents=bubble)
        return message

    # no face detected
    def no_face(self):
        bubble = BubbleContainer(
            # header
            header=BoxComponent(
                layout='horizontal',
                contents=[
                    TextComponent(text='No face detected', size='lg', color='#5b5b5b')
                ]
            ),

            # hero
            hero=ImageComponent(url='https://i.imgur.com/cIGrXmq.png', size='xl', aspect_ratio='4:4', aspect_mode='cover'),

            # body
            body=BoxComponent(
                layout='vertical',
                spacing='md',
                contents=[
                    
                    SeparatorComponent(margin='md'),

                    BoxComponent(
                        layout = 'horizontal',
                        spacing='md',
                        contents = [
        
                            TextComponent(text='很抱歉, 圖片未偵測到臉部,\n 請考慮環境因素影響(如燈光)、臉部角度等因素或確認圖中是否有人臉。\n\nPlease try again. Thanks for your cooperation.', size='sm', wrap=True, color='#9d9d9d', align='center')
                        ]
                    )
                ]
            )
        )
        message = FlexSendMessage(alt_text="No face detected", contents=bubble)
        return message

    # many faces detected
    def too_many_faces(self):
        bubble = BubbleContainer(
            # header
            header=BoxComponent(
                layout='horizontal',
                contents=[
                    TextComponent(text='Multiple face detected', size='lg', color='#5b5b5b')
                ]
            ),

            # hero
            hero=ImageComponent(url='https://i.imgur.com/2X6jdIK.png', size='xl', aspect_ratio='4:4', aspect_mode='cover'),

            # body
            body=BoxComponent(
                layout='vertical',
                spacing='md',
                contents=[
                    
                    SeparatorComponent(margin='md'),

                    BoxComponent(
                        layout = 'horizontal',
                        spacing='md',
                        contents = [
        
                            TextComponent(text='很抱歉, 目前暫不支援多臉辨識，\n請確認圖片中只有一張臉，謝謝。\n\nPlease try again. Thanks for your cooperation.', size='sm', wrap=True, color='#9d9d9d', align='center')
                        ]
                    )
                ]
            )
        )
        message = FlexSendMessage(alt_text="Multiple Face detected", contents=bubble)
        return message

    # intro
    def intro(self, user_name):
        bubble = BubbleContainer(
            # header
            header=BoxComponent(
                layout='horizontal',
                contents=[
                    TextComponent(text='Hi {0},'.format(user_name), size='lg', color='#000000')
                ]
            ),

            # hero
            hero=ImageComponent(url='https://i.imgur.com/xYgkKHe.png', size='full', aspect_ratio='16:9', aspect_mode='cover'),

            # body
            body=BoxComponent(
                layout='vertical',
                spacing='md',
                contents=[
                    
                    SeparatorComponent(margin='md'),

                    BoxComponent(
                        layout = 'horizontal',
                        spacing='md',
                        contents = [
        
                            TextComponent(text='Hi 可以發一張圖片給我，\n我能識別出裡面的人臉情緒唷～\n\n', size='md', wrap=True, color='#272727', align='center')
                        ]
                    ),

                    BoxComponent(
                        layout = 'horizontal',
                        spacing='md',
                        contents = [
        
                            TextComponent(text='聲明\n辨識完即刪除，不會以任何形式保存圖片、人像等敏感性資訊', size='sm', wrap=True, color='#00BE00', align='center')
                        ]
                    )            

                ]
            )
        )
        message = FlexSendMessage(alt_text="hello~", contents=bubble)
        return message