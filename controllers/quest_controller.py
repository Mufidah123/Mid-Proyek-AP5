# Controller for quest
import random
from models.quest_model import QuestData
from controllers.leaderboard_controller import update_player_score

class QuestController:
    def __init__(self, character):
        self.character = character
        self.active_quest = None

    # Membuat quest baru
    def bikin_quest(self):
        # Jika sudah menyelesaikan 3 quest biasa, munculkan quest boss
        if self.character.quest_selesai >= 3:
            self.buat_quest_boss()
            self.character.quest_selesai = 0  # reset counter setelah boss
            return

        tipe_quest = random.choice(["berburu", "pengumpulan"])
        kesulitan = random.choice(["mudah", "sedang", "sulit"])
        pengali = {"mudah": 1, "sedang": 1.5, "sulit": 2}[kesulitan]

        if tipe_quest == "berburu":
            musuh = random.choice(["goblin", "serigala", "bandit", "orc", "naga kecil"])
            gold_reward = int(random.randint(5, 15) * pengali)
            exp_reward = int(random.randint(10, 25) * pengali)
            quest = QuestData("berburu", f"Lawan {musuh}", gold_reward, exp_reward, kesulitan)
        else:
            material = random.choice(["kayu", "batu sihir", "herbal", "kulit binatang", "biji besi"])
            gold_reward = int(random.randint(3, 10) * pengali)
            exp_reward = int(random.randint(8, 20) * pengali)
            quest = QuestData("pengumpulan", f"Kumpulkan {material}", gold_reward, exp_reward, kesulitan)

        self.active_quest = quest
        print("\n🧭 Quest Baru Diterima!")
        quest.tampilkan_info_quest()

    # Membuat quest boss
    def buat_quest_boss(self):
        bos = random.choice(["Naga Api", "Raja Orc", "Iblis Kegelapan", "Hydra"])
        print("\n🔥 QUEST BOSS TERBUKA! 🔥")
        hadiah_uang = random.randint(50, 100)
        hadiah_exp = random.randint(150, 250)
        quest_boss = QuestData("boss", f"Kalahkan {bos}", hadiah_uang, hadiah_exp, "epik")
        self.active_quest = quest_boss
        self.character.bisa_lawan_boss = True
        quest_boss.tampilkan_info_quest()

    # Menyelesaikan quest
    def selesaikan_quest(self):
        if not self.active_quest:
            print("❌ Tidak ada quest aktif!\n")
            return

        print(f"Menjalankan quest: {self.active_quest.nama}...")
        hasil = random.choices(["berhasil", "gagal"], weights=[0.8, 0.2])[0]

        if hasil == "berhasil":
            # Tambahkan gold & exp
            self.character.uang += self.active_quest.hadiah_uang
            self.character.pengalaman += self.active_quest.hadiah_exp
            print(f"✅ Quest berhasil! Kamu mendapat {self.active_quest.hadiah_uang} gold dan {self.active_quest.hadiah_exp} exp.")

            # Tambahkan skor berdasarkan jenis quest
            if self.active_quest.tipe == "boss":
                self.character.skor += 100  # skor besar untuk boss
                self.level_up_setelah_boss()
            else:
                base_score = {"mudah": 10, "sedang": 20, "sulit": 30}[self.active_quest.kesulitan]
                self.character.skor += base_score
                self.character.quest_selesai += 1
                print(f"📜 Quest selesai: {self.character.quest_selesai}/3 sebelum boss muncul.")
                print(f"🏆 Skor +{base_score} (Total: {self.character.skor})")

            # Update skor ke leaderboard
            update_player_score(self.character.user_id, self.character.skor)

        else:
            print("❌ Quest gagal! Tidak mendapat hadiah.")
            self.character.skor -= 5

        self.active_quest = None
        print(f"💰 Gold: {self.character.uang} | ⭐ EXP: {self.character.pengalaman} | 🏆 Skor: {self.character.skor}\n")

    # Naik level setelah boss dikalahkan
    def level_up_setelah_boss(self):
        print("👑 Kamu mengalahkan BOS! Pengalaman dan hadiah besar diterima.")
        self.character.level += 1
        self.character.gelar = random.choice(["Pahlawan", "Sang Penakluk", "Kesatria Agung", "Pembasmi Kegelapan"])
        self.character.bisa_lawan_boss = False
        print(f"🎉 LEVEL UP! Sekarang Level {self.character.level} - Gelar: {self.character.gelar}")
        print(f"🏆 Bonus Skor +100 (Total: {self.character.skor})\n")
