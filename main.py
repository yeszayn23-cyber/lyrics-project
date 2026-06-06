from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
# هنا نقوم باستيراد البيانات من ملف config الذي أنشأتِه
from config import TOKEN, ADMIN_ID

bot = Bot(token=TOKEN)
dp = Dispatcher()

# هذا الأمر هو الاختبار الأول لكِ كأدمن
@dp.message(Command("add_button"))
async def add_button_command(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("أهلاً يا أدمن! معكِ كل الصلاحيات. ما هو اسم الزر الذي تريدين إضافته؟")
    else:
        await message.answer("عذراً، هذه الصلاحية للمديرة فقط.")

async def main():
    print("البوت يعمل الآن...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
