def info(class_name):
    if class_name == "unknown_class":
        pic = "static/unknown_pic.jpg"
        desc = "Unknown Image. please select or take a valid image.\n the image you provided is either an image of sculpture unlabeled by this application yet or is an image unrelated to this application usage."
        desc2 = "please select or take a valid image.\n the image you provided is either an image of sculpture unlabeled by this application yet or is an image unrelated to this application usage."
        content = "No information"
        return pic, desc, desc2, content
    pic = f"static/{class_name}_pic.jpg"
    if class_name == "Vishnu":
        desc = "Vishnu is one of the principal deities of Hinduism, known as the Preserver within the Trimurti (the Hindu trinity). Vishnu is believed to embody compassion and protection, and he periodically takes on earthly avatars to restore balance to the world."
        desc2 = "Hinduism reached Southeast Asia, including Cambodia (formerly known as Khmer Empire), around the 1st century CE. Vishnu quickly became a prominent deity, alongside Shiva, the Destroyer.Khmer kings associated themselves with Vishnu, claiming divine authority through their connection to the preserver god. This association helped solidify their rule and promote social order."

        
    
    elif class_name == "Lakshmi":
        desc = "Lakshmi is the Hindu goddess of wealth, fortune, and prosperity. She is a symbol of beauty, abundance, and auspiciousness."
        desc2 = "Lakshmi's importance lies in her association with wealth and material prosperity – essential aspects Khmer kings sought for their kingdom.Lakshmi's grace and regal iconography resonated with depictions of powerful queens, highlighting their importance in maintaining social harmony and prosperity within the kingdom."


    elif class_name == "Shiva":
        desc = "Shiva is one of the supreme deities of Hinduism, known as 'The Destroyer' within the Trimurti. Despite his destructive association, Shiva also represents transformation, rejuvenation, and the cycle of life and death."
        desc2 = "Unlike other regions where Vishnu held equal or greater importance, Shiva reigned supreme in the Khmer pantheon. He was seen as the source of all creation and the ultimate force behind change and transformation.Khmer kings identified with Shiva's ascetic aspects, such as self-discipline and yogic practices. This association reflected the ideal of a righteous and dedicated ruler who ensured prosperity for his people."

        
    elif class_name == "Monivong":
        desc = "Sisowath Monivong was the King of Cambodia from 1927 until his death in 1941, ruling during the period of French colonial influence."
        desc2 = "Monivong took a strong interest in preserving and revitalizing Khmer culture. He supported the study of Khmer history, the arts, and the restoration of important historical sites.While politically limited, Monivong supported some social and administrative reforms, aiming to modernize Cambodia within the constraints of the colonial system."

    
    elif class_name == "Buddha":
        desc = "The Buddha, originally named Siddhartha Gautama, was a spiritual teacher who lived in ancient India.His teachings form the foundation of Buddhism, a major world religion emphasizing mindfulness, compassion, and the end of suffering."
        desc2 = "Early depictions of Buddha in Khmer art show the influence of Indian and Southeast Asian styles. Later periods reflect distinct Khmer artistic interpretations of the Buddha's form, often serene and meditative.Khmer depictions of Buddha incorporate traditional Buddhist iconography such as the ushnisha (cranial bump), elongated earlobes, mudras (hand gestures), and the lotus flower representing purity."

    
    elif class_name == "Harihara":
        desc = "Harihara (Sanskrit: हरिहर) is the dual representation of the Hindu deities Vishnu (Hari) and Shiva (Hara). Harihara is also known as Shankaranarayana ('Shankara' is Shiva, and 'Narayana' is Vishnu). Harihara is also sometimes used as a philosophical term to denote the unity of Vishnu and Shiva as different aspects of the same Ultimate Reality called Brahman. This concept of equivalence of various gods as one principle and 'oneness of all existence' is discussed as Harihara in the texts of Advaita Vedanta school of Hindu philosophy."
        desc2 = "Harihara, a deity blending aspects of both Vishnu and Shiva, held significant influence within the Cambodian Khmer Empire. This influence arose from kings associating themselves with Harihara, embodying their power and role in upholding cosmic balance. Harihara's syncretic nature mirrored Cambodia's own blend of Hinduism and Buddhism.  Temples were adorned with intricate Harihara imagery, reflecting the deity's importance."
    
    elif class_name == "Lokeshvara":
        desc = 'In Buddhism, Avalokiteśvara (meaning "the lord who looks down", IPA: /ˌʌvəloʊkɪˈteɪʃvərə/[1]), also known as Lokeśvara ("Lord of the World") and Chenrezig (in Tibetan), is a tenth-level bodhisattva associated with great compassion (mahakaruṇā). He is often associated with Amitabha Buddha.[2] Avalokiteśvara has numerous manifestations and is depicted in various forms and styles. In some texts, he is even considered to be the source of all Hindu deities '
        desc2 = 'Lokeshvara, the embodiment of compassion in Mahayana Buddhism, held significant sway within the Khmer Empire.  The veneration of Lokeshvara, particularly  during the 12th and 13th centuries, reflected a period when Mahayana Buddhism thrived in Cambodia. '
    
    elif class_name == "Ganesha":
        desc = "Ganesha, the elephant-headed god, is one of the most beloved and easily recognized deities within the Hindu pantheon. He is revered as the remover of obstacles, the patron of wisdom, beginnings, arts, and sciences. Ganesha's unique appearance, with his human body and elephant head, coupled with his mischievous yet benevolent nature, has made him a widely popular figure within Hindu mythology and devotional practices."
        desc2 = "Ganesha's influence extended to ancient Cambodia, likely introduced through trade routes and cultural exchange with India. His popularity stemmed from his connection to success and overcoming obstacles, making him particularly appealing to merchants and those seeking prosperity. Ganesha shrines and depictions were found in both temples and more modest settings, indicating his widespread veneration across different social strata."
    
    elif class_name == "Brahma":
        desc = "In Hinduism, Brahma holds the esteemed position as the creator god within the trinity of supreme deities (Brahma, Vishnu, and Shiva). He represents the generative principle of the universe, the source from which all existence springs. While frequently depicted with four heads and four arms, representations of Brahma also include his association with the lotus flower and sacred texts."
        desc2 = "Brahma's legacy is intertwined with the history of pre-Buddhist Cambodia, particularly during the formative phases of the Khmer Empire. His veneration was likely tied to the early Hindu influence from India, with Khmer kings often associating themselves with deities like Brahma to legitimize their rule. Artistic representations of Brahma adorned temples and palaces, emphasizing his status as a revered figure in Cambodian society."
    
    elif class_name == "Jayavarman_VII":
        desc = "Jayavarman VII stands as one of the most powerful and revered monarchs of Cambodia's Khmer Empire. His reign (c. 1181 - 1218 CE) was a period of territorial expansion, remarkable architectural achievements, and a shift towards Mahayana Buddhism. He is remembered for his military prowess, particularly in ousting the Cham invaders, as well as his unwavering devotion to Buddhism."
        desc2 = "Jayavarman VII's legacy on Cambodia is profound. His extensive building projects, including the iconic Bayon temple, Angkor Thom, and a network of hospitals and rest houses, reshaped the landscape. His embrace of Buddhism as the state religion fostered a significant shift in Cambodian spiritual life. Jayavarman VII's commitment to his people's well-being, reflected in his public works projects, solidified his image as a compassionate and benevolent ruler."
    
    elif class_name == "Hanuman":
        desc = "Hanuman, the revered monkey deity, is a central figure in the Hindu epic Ramayana. He is known for his unwavering devotion to Lord Rama, his extraordinary strength, courage, and his ability to shapeshift.   Often depicted with a powerful physique and a monkey's head, Hanuman symbolizes loyalty, selfless service, and the triumph of good over evil."
        desc2 = "Hanuman's influence in Cambodia is significant due to the popularity of the Ramayana and its Cambodian adaptation, the Reamker. His exploits in aiding Rama and his embodiment of virtues made him an immensely popular figure. Hanuman's presence is woven into Cambodian art, dance, and folklore. Temples often feature depictions of Hanuman, and he is a central character in the traditional dance-drama, the Robam Sovann Maccha."
    
    
    with open(f"text/{class_name}.txt", "r") as file: 
        content = "".join(line for line in file)

        
    return pic, desc, desc2, content
