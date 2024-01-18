from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

CEO = env.int("CEO")
ACADEMIC_DEPARTMENT = env.int("ACADEMIC_DEPARTMENT")
ADMIN_DEPARTMENT = env.int("ADMIN_DEPARTMENT")
SALES = env.int("SALES")
MARKETING = env.int("MARKETING")
AXO = env.int("AXO")

departments = [CEO, ADMIN_DEPARTMENT, ACADEMIC_DEPARTMENT, SALES, MARKETING, AXO]