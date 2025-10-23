music = {
    "stealth": "https://www.youtube.com/watch?v=U47Tr9BB_wE",
    "march": "https://www.youtube.com/watch?v=Xqeq4b5u_Xw",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI&pp=ygUHc2t5ZmFsbA%3D%3D",
    "wolf": "https://www.youtube.com/watch?v=ThCH0U6aJpU&list=PLnrGi_-oOR6wm0Vi-1OsiLiV5ePSPs9oF&index=21",
    "mohra": "https://www.youtube.com/watch?v=Zd0dI8LqxDw"
}

#deepseek setup
# def aiProcess(command):
#     try:
#         response = client.chat.completions.create(
#             model="deepseek-chat", 
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant named Friday. Give short and useful two-line replies only."},
#                 {"role": "user", "content": command},
#             ],
#             stream=False
#         )
#         reply = response.choices[0].message.content
#         print("AI Response:", reply)
#         return reply

#     except Exception as e:
#         print("AI Error:", e)
#         return "AI response failed."
# from openai import OpenAI
# def aiProcess(c):
#     try:
#         client = OpenAI(api_key="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")
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant named Friday. Give short and useful two-line replies only."},
#                 {"role": "user", "content": c}
#             ]
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         print("AI Error:", e)
#         return "AI response failed."