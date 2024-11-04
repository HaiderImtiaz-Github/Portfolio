class Profile:
    def __init__(self, experience, specialization, expertise, leadership):
        self.experience = experience
        self.specialization = specialization
        self.expertise = expertise
        self.leadership = leadership

    def describe(self):
        return (f"I have {self.experience}, specializing in {self.specialization}. "
                f"I am an expert in {self.expertise}. "
                f"A proven leader in {self.leadership}.")

# Define 'I' as an instance of Profile
I = Profile(
    experience="over 6 years of experience in the Ministry of Defense",
    specialization="logistics, technical support, and human resource management",
    expertise="logistic support plans, equipment readiness, and field exercise logistics",
    leadership="technical briefings, solar projects, and managing over 150 personnel"
)

# Print the description for the portfolio
print(I.describe())
