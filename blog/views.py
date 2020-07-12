from django.shortcuts import render
from .models import Post
# Create your views here.
def host(request):
    Post.objects.create(
        id=1,
        catalog='choice',
        catagory='Alternative Materials',
        image='c1.jpg',
        question='Have you tried out different possible materials and thought about implications at various stages during the life cycle of a clothing product?',
        description='Everyday waste can potentially be transformed into valuable ingredients for your design object or service system. Fashion designer Emily Crane designed cultivated couture from everyday cooking ingredients such as gelatines, kappa carrageenan, agar-agar seaweed,water,natural flavour extracts,glycerine, food colouring and lustres. Every day cooking ingredients transform into hightech kitchen couture.')
    Post.objects.create(
        id=2,
        catalog='choice',
        catagory='Alternative Energies',
        image='c2.PNG',
        question='Can your design minimise energy use in the design process and maximise the life of the garment using alternative energy resources?',
        description='Sunlight can be a major resource of natural energy for utilisation. The Zegna designed Eco-tech Solar Jacket, made from 100% recycled plastic sources and a detachable solar cell sleeves,can convert sunlight into renewable energy. It can also keep the body warm and charges the battery pack that can hold enough electricity to recharge a cell phone or iPod. This is done with 5 hours of sunlight.')
    Post.objects.create(
        id=3,
        catalog='choice',
        catagory='Alternative Process',
        image='c3.png',
        question='How can innovative thinking and new technologies help you to rethink materials and process?',
        description='Technological innovations and creative thinking can create new materials that can be grown, cooked or become selfsufficient. Artist Donna Franklin and scientist Gary Cass explore the idea of growing seamless biosynthetic materials from cellulose microfibrils; Suzanne Lee has coined the name ‘bio-couture’ for her clothes grown from microbialcellulose')
    Post.objects.create(
        id=4,
        catalog='choice',
        catagory='Alternative Cloth Packaging',
        image='c4.PNG',
        question='How can you design alternative ways of packaging clothing to minimise waste?',
        description='Rethinking clothing packages can solve three common product design problems at once. Hangerpack suggested a clothing package design that provides flexible packaging for shipping is easy to recycle at the end of life cycle stage and transforms into a reusable object (hanger) in the package.')
    Post.objects.create(
        id=5,
        catalog='choice',
        catagory='Alternative Distribution',
        image='c5.PNG',
        question='Can you design alternative distribution services and systems for the product?',
        description='One of the main criticisms of the circular economic approach is that if all the products have to be sent back to producers for reuse or remanufacturing, the transportation will be considerably increased. Moreover, remanufacturing activities often cost more than production of products from virgin raw materials.Alternative ways of distribution using local supplier and distribution enable you to reduce transportation and create jobs for the local community.')
    Post.objects.create(
        id=6,
        catalog='choice',
        catagory='Ways of Buying Sustainably',
        image='c6.PNG',
        question='How can your design enforce sustainable consumption behaviour?',
        description='Current consumption patterns are crucial causes of environmental and social problems and consumer behaviour is central to society’s impact on the environment (Jackson, 2005). Considering how and where clothing is made, who it is made by and rethinking consumption activities can play a critical role in supporting sustainability. Designers can also provide effective instructions for efficient and environmentally friendly use')
    Post.objects.create(
        id=7,
        catalog='choice',
        catagory='Ways of Wearing Garments',
        image='c7.PNG',
        question='Have you suggested alternative uses for your clothing to develop your unique individual look using your existing clothing rather than buying more?',
        description='People can have a limited perception about what can be worn. If a designer makes clothing with a more flexible approach, people can be encouraged to wear things differently. Uniform project is a one-year fundraiser for the education of underprivileged children in India, where they designed a dress to wear 365 days as an exercise in sustainable fashion. How creative can you be with how your piece of clothing can be worn?')
    Post.objects.create(
        id=8,
        catalog='choice',
        catagory='Ways of maintaining',
        image='c8.PNG',
        question='How can you extend the length of clothing life and make the clothing user think of their garments as more valuable?',
        description='Exploring new ways of maintaining and manipulating existing products can extend product life as well as add new value to the product during the design process. Use of organic, bio- or renewable materials which are more sustainable, means the clothing can be maintained, re-used or repaired by users infinitely. It also allows disassembly or re-assembly according to users’ mood or accession')
    Post.objects.create(
        id=9,
        catalog='choice',
        catagory='Ways of washing clothes',
        image='c9.jpg',
        question='How can your design influence positive behaviour in laundering to deal with future water shortages and high energy consumption?',
        description='One of major environmental impact of clothing comes from laundering and aftercare during the consumer use stage (Cited in Fletcher, 2008). Designers can trigger pro-environmental behaviour through suggestion of alternative designs including modular or badge type and only the dirty part of the garment has to be washed. Fletcher proposed the design that is not to resist or repel dirt, but to wear it like a badge. She documented the response to this idea in a laundry diary over six months')
    Post.objects.create(
        id=10,
        catalog='choice',
        catagory='Ways of Relinquishment',
        image='c10.jpg',
        question='How can the impact of clothing disposal be reduced?',
        description='Only around 15% of disposed clothing and textiles in the UK are collected for reuse and recycling at present. 70% is sent to landfill (60%) or incineration (10%) (Forum for the Future, 2007). When rethinking our clothing disposal behaviour, the designer can suggest different possibilities of disposing methods such as reuse, converting garment for another purpose or making clothes easy to recover for remanufacturing, trading or selling. E.g. Wearable Collections provides a useful solution by collecting clothing for recycling in NYC.')
    Post.objects.create(
        id=11,
        catalog='Optimisation',
        catagory='Rethink Grit',
        image='o1.jpg',
        question='Can the use of durable materials support the sustainability of long-lived garments?',
        description='Fashion product life has become extremely short and people often discard clothing because they are tired of existing clothing or it is out of fashion. Helen Storey (2008) designed disposable short life clothing through suggesting the wider issues of sustainability and ethical living.')
    Post.objects.create(
        id=12,
        catalog='Optimisation',
        catagory='Biomimicry',
        image='o2.jpg',
        question='How could you apply biomimicry to make fashion and textiles products as sustainable as natural systems?',
        description='Benyus (2002) suggests that looking to nature could solve human problems and contribute great "levels of innovation". The main idea of biomimicry is to understand nature’s biological principles and apply problem solving ideas to develop innovative new materials, production processes and design systems.')
    Post.objects.create(
        id=13,
        catalog='Optimisation',
        catagory='Cradle to Cradle',
        image='o3.jpg',
        question='Can you optimize product design to maximize reusability?',
        description='Adapting metabolism concepts, ‘Cradle to Cradle’ (McDonough and Braungart , 2002) suggest a whole system view of design which extends product life beyond a first life into the next cycle of life where waste is reconceived as a useful and valuable component of another product’s future life. A biological nutrient can be designed to return to the biological cycle and can be safely biodegradable. A technical nutrient is a product designed to go back into the technical cycle; for example it may be disassembled and the parts re-used.')
    Post.objects.create(
        id=14,
        catalog='Optimisation',
        catagory='Modularity',
        image='o4.jpg',
        question='Is your product moveable and adaptable? Can it be disassembled by the user? If so, how does it promotes sustainability?',
        description='Modular systems embrace the concept of “minimum inventory and maximum diversity”. Modular pieces can be combined or taken apart at the will of the user, allowing the product to be co-created by designer and consumer as part of a unique experience. The design practice could encourage the end-user to participate in design process through a flexible approach to creation. E.g.) Eunsuk Hur ‘s Transformative modular textiles.')
    Post.objects.create(
        id=15,
        catalog='Optimisation',
        catagory='Merging',
        image='o5.png',
        question='Can your project decrease the flow of production and increase consumer interaction with your design? Can you skip similar parts of production process and share similar characteristics?',
        description='Merging similar processes or parts to perform parallel operations through adaption of technologies and innovative thinking can help to decrease the production flow and garment waste. E.g.Constructible clothes.')
    Post.objects.create(
        id=16,
        catalog='Optimisation',
        catagory='Zero-waste',
        image='o6.png',
        question='How can you eliminate fabric waste during pattern making and create environmental and economic benefit?',
        description='The creation of fabric waste resides within fashion design and patternmaking, which generates 10 to 20 percent of fabric scrap (Rissanen, 2008). Mark Liu (2007) suggested Zero waste fashion through designing the garment pattern and the printed textile simultaneously; hence the entire textile piece becomes the dress without creating fabric waste. There are still issues regarding clothing size and limited styles.')
    Post.objects.create(
        id=17,
        catalog='Optimisation',
        catagory='Vital Upgrade',
        image='o7.png',
        question='How can you provide dynamic upgradable fashion to the user, so that consumers can upcycle multiple times?',
        description='If a designer provides a dynamic upgradable system, the consumer could buy fewer quality garments with the expectation of upgrading and refashioning them over again rather than buying new clothing.')
    Post.objects.create(
        id=18,
        catalog='Optimisation',
        catagory='Multi Fashion',
        image='o8.png',
        question='Can you make a multifunctional apparel design or fashion system so people can use it for a different purpose, or produce an alternative product?',
        description='Transformative multi- functional clothing can be one of the tools to trigger emotional attachment over an extended period of time. This emotional response could be extended from one occasion to various others beyond conventional rules of style')
    Post.objects.create(
        id=19,
        catalog='Optimisation',
        catagory='Update System',
        image='o9.PNG',
        question='Can your designed product allows the user to make continuous process improvements through up-cycling?',
        description='Designers can encourage the user to rethink how they can mend, repair and up cycle with reclaimed garments. Earley has been exploring the idea of up cycling textile and clothing since 1999 as a digital sketchbook records the making and development of the Top 100 projects. Her project is practice-based textile and fashion design research which divides the 100 shirts into a series of refashioning methods.')
    Post.objects.create(
        id=20,
        catalog='Optimisation',
        catagory='Swap & Share',
        image='o10.webp',
        question='What are the potential opportunities to support sustainability in the fashion and textile design through swap & share service design?',
        description='Service design can has considerable sustainability potential through providing opportunities to meet needs with fewer resources and less energy. (for example, clothing libraries and clothing swapping services, product to service shifts for classic items–hiring desired fashion items for a short period of time)E.g.keep & share offers quality pieces and versatile products that can be worn in different ways and by different people over their lifetimes.')
    Post.objects.create(
        id=21,
        catalog='Empowerment',
        catagory='Storytelling',
        image='e1.jpg',
        question='How can your design influence multiple people and connect them with their emotions?',
        description='Storytelling allows new discoveries of personal value with a more empathic experience that leads to emotional attachment to the user. Marie Ilse Bourlanges explored the idea of anticipation of the decay through investigation of the human movement and the relationships between notions of time, body, skin and clothes and intended to express the broad semantic of decay. Bourlanges captured the gestures of body bending and trace of time in the garment which potentially anticipated eventual decay of the textile and human body movement of daily life')
    Post.objects.create(
        id=22,
        catalog='Empowerment',
        catagory='Magic',
        image='e2.jpg',
        question='Can your design evoke a magical experience and curiosity, like marrying traditional design skills with advanced technologies?',
        description='The Magic element in the design process allows numerous user engagements and experiences; the resultant product is likely to be emotionally connected to the consumer (Chapman, 2005). Ezgihan Talay explored the idea of ‘Movement and Interactivity’ through using Nintendo Wii to update the experiential marbling art, the outcome of the movements is translated to the fabrics. This incorporated new technique allows anyone to easily alter the artwork by moving white-gloved hands')
    Post.objects.create(
        id=23,
        catalog='Empowerment',
        catagory='Poetic',
        image='e3.jpg',
        question='Can your design trigger memory as a poetic experience and evoke personal intimacy?',
        description='The poetic pattern can promote emotional bonds with the object which encourages on-going use, enduring values within products. This poetic element sustains the slow passing of time and an overall sensitivity to how fabrics and garments are actually used. Veasyble is a conceptual set of accessories that transform to create an intimate world for the wearer at a moment’s notice as symbolic representations, but contribute to the user’s experience of the world around them')
    Post.objects.create(
        id=24,
        catalog='Empowerment',
        catagory='Playfulness',
        image='e4.png',
        question='How can you maximise playful experiences through visual appearance, usability, service, process, materials etc.?',
        description='Playful experiences provoke curiosity and emotional attachment with the user. Elisabeth Buecher designed a series of costumes, ‘Siamese Accessories’ which only functions if worn by two people at the same time. This playful experience provides two users to become Siamese twins and formed new creatures.')
    Post.objects.create(
        id=25,
        catalog='Empowerment',
        catagory='Personality',
        image='e5.jpg',
        question='Can you suggest a platform that allows the user to show facial expressions through the use of their own personal avatar which depend on the user’s personality or characters?',
        description='Fashion service provides a personalised clothing avatar and allows any accessory and clothing to be tried on through a virtual experience. GirlSense Design Studio allows creation of personalised clothing depending on the mood. This platform allows the user to show facial expressions through the use of their own personal avatar.')
    Post.objects.create(
        id=26,
        catalog='Empowerment',
        catagory='Partial Fruition',
        image='e6.jpeg',
        question='Can your design be rearranged in various configurations or semi-finished platforms according to individual needs, so that people could contribute to the design process?',
        description='People are used to having ‘perfect’ looking fashion through ready-made products. Walker (2006) suggested that partial completion could encourage people‘s care and maintenance of our material environment and contributes to product longevity. Hanna Nyman creates 3D wall papers which give unique experience and personal user touch in product.')
    Post.objects.create(
        id=27,
        catalog='Empowerment',
        catagory='User as maker',
        image='e7.PNG',
        question='Can consumers become co-partners in your design process? Might this encourage more sustainable consumption?',
        description='A widespread DIY (Do it yourself) culture and microproduction gives the opportunity to everyone to become a creator and social actor in design. This movement develops competent individuals who have the potential to produce their clothes or supply skills and resources to others, enabling them to create as well as consume. E.g.) Craft DIY community')
    Post.objects.create(
        id=28,
        catalog='Empowerment',
        catagory='Smart Craft',
        image='e8.jpg',
        question='Can you use your design process as an educational and experimental tool in which the user can easily learn to use new technologies and science for their own project?',
        description='Smart craft gives people the opportunity to work with science and technology in an easy and enjoyable way to create new ideas. Technologies such as, LilyPad Arduino encourages active participation with DIY Community. People can learn and share their knowledge about smart materials and new technologies for their own fashion design.')
    Post.objects.create(
        id=29,
        catalog='Empowerment',
        catagory='Unseal Fashion',
        image='e9.png',
        question='How can open source support reshaping the meaning of innovation through socially engaged process with a wide range of actors?',
        description='Open source fashion has been transformed in craft and design as social dimensions of activities, derived from digital technology which opened up a range of new media deliver to consumers and the creative industries. This shift change design practices in production and development that promote access to the end products source materials. Growing open source design provides an open digital designing service for micro-manufacturing.')
    Post.objects.create(
        id=30,
        catalog='Empowerment',
        catagory='Pursue Creativity',
        image='e10.jpg',
        question='Can your design system provide a way to become more creative and get inspired to create?',
        description='Studio Ludens help anyone explore their own creativity through providing the digital design tool. Their aim is to serve people the creative freedom and promoting the use and re-use of customised design. The online tool enables people to get involved with some 2D geometry to CAD programming which is then applied to laser-cutting, fabric printing, and weaving.')
    Post.objects.create(
        id=31,
        catalog='persuasion',
        catagory='Informative',
        image='p1.png',
        question='How can you make more informed choices for producers and consumers?',
        description='Education is one of critical elements for facilitating sustainable fashion design. It is capable to persuade people to address sustainability issues associated in fashion design. Fashioning an Ethical Industry (FEI) provides useful education resources, student workshops in order to promote sustainability in the industry. FEI works with educators and students on fashion related courses in order to raise awareness of a global overview of the fashion industry and fashion design practices.')
    Post.objects.create(
        id=32,
        catalog='persuasion',
        catagory='Guidance',
        image='p2.PNG',
        question='Can your design offer the appropriate guidance to the user?',
        description='Eco-labels and certification can help inform guidelines and choices for consumers who want to buy eco-friendly products. Furthermore, the designer can provide more product information in the integrated labels with a garment’s history such as designer’s intention, life time with garment, material properties, laundry method, and updatable methods. For example, the Fair trade Labeling Organisation (FLO) provides useful information regarding cotton production processes.')
    Post.objects.create(
        id=33,
        catalog='persuasion',
        catagory='Story of Use',
        image='p3.png',
        question='Can your design scenario promote a more sustainable way of living in the context of their everyday behaviour as a story?',
        description='The use of innovative story and awareness-raising campaigns enable and encourage people to lead more sustainable life stylese.g. Green thing provide unique videos and inspiring stories from creative people and community members around the world, aiming to inspire people to lead a greener life')
    Post.objects.create(
        id=34,
        catalog='persuasion',
        catagory='Transparency',
        image='p4.PNG',
        question='Can you make your design more transparent by revealing under the surface of the design process? Can this be used to influence user’s perceptions and behaviour?',
        description='Transparency is one of the vital aspects to create brand loyalty and encouraging sustainable design practices. Made-By label is a non-profit organisation involved with a fashion brand to show the entire production process behind a product including from raw materials through to the finished product which aims to improve environmental and social conditions in the fashion industry. Made-by label encourages transparency of supply chain and openness leading to more sustainable design practices')
    Post.objects.create(
        id=36,
        catalog='persuasion',
        catagory='Reinforcement',
        image='p6.jpg',
        question='Can you emphasise the new possibility of resources and increase awareness of value of resource use through your design?',
        description='Hyun-Jin Jeong explored the potential of earth as a material for textile design and colouration through various dyeing and printing experimentations. She emphasised the alternative possibility for dyeing colouration and new aesthetic values of natural material using 45 different soils collected from varied geographical locations')
    Post.objects.create(
        id=35,
        catalog='persuasion',
        catagory='Warning',
        image='p5.jpg',
        question='Does your design give information regarding the usage of the garment?',
        description='Critical reflection on the design process and interactive design process enables people to understand the issue of user’s energy use and take control in their actions. For example, a pollution sensing and visualising garment (CO2- dress) has been designed by collaboration between diffus.')
    Post.objects.create(
        id=39,
        catalog='persuasion',
        catagory='Commitment',
        image='p9.jpg',
        question='How can your design create a dialogue with the user that encourages responsible use of products? How could we actively promote reliable garments?',
        description='The Clean Clothes Campaign support and promote the fundamental rights of workers in the global garment and sportswear industries. They educate consumers, lobby companies and governments, and offer direct solidarity support to workers as they fight for their rights and demand better working conditions')
    Post.objects.create(
        id=37,
        catalog='persuasion',
        catagory='Reward',
        image='p7.PNG',
        question='Can you encourage the user to participate in continuous positive action through a series of rewards or incentives when they achieve positive action in your system?',
        description='Reward and incentive can instantly motivate people to adopt pro-environmental behaviours. ‘Fashioning the Future Awards’ encourage designers to create innovative sustainable fashion design through engaging the participation of students and graduates from across the world.')
    Post.objects.create(
        id=38,
        catalog='persuasion',
        catagory='Simplicity',
        image='p8.PNG',
        question='Can you simplify your design system or service to be easier, so that people’s behaviour can adapt to habitual routine?',
        description='If the design process is simple and easy to adopt, people tend to change behaviour more effectively and act over and over again in a habitual routine. In pursuing simplicity, people have a tendency to stick to their routine (Fogg, 2009).')
    Post.objects.create(
        id=40,
        catalog='persuasion',
        catagory='Backer Incentive',
        image='p10.jpg',
        question='Can your design promote continuous improvement of shareholder value?',
        description='Sony and the Solar-bear Foundation made a partnership which aims to encourage consumers to participate in an environmental conservation activity when they buy batteries. A picture book featuring the cubs is available to help parents educate their children about climate change and its effects (cited in WBCSD, 2008)')
    Post.objects.create(
        id=41,
        catalog='Interaction',
        catagory='Sensory Effect',
        image='i1.PNG',
        question='How can the use of sensory effects (sound, light, smell, etc.) encourage users to interact or behave more positively?',
        description='Sensory experiences trigger emotions, sentimentality and memories for the user and help to reduce cognitive effort for behavioural change. Jenny Tillotson explored the multi-sensory enhancement through suggesting the smart second skin dress which allows the wearer to enter a sixth dimension by creating a rainbow symphony of aromas.')
    Post.objects.create(
        id=42,
        catalog='Interaction',
        catagory='Variable Change',
        image='i2.jpg',
        question='How can you control user behaviour automatically through design combined with advanced technology?',
        description='Changing an objects physical state (e.g. to a gas, liquid, or solid), changing the degree of flexibility or changing the temperature. The life-span of ordinary things and everyday life may be transformed in relation to existent energy conditions. Kerri Wallace explored idea of the human motion response incorporating it with thermo-chromic and liquid crystal heat responsive technology.')
    Post.objects.create(
        id=43,
        catalog='Interaction',
        catagory='Primary Action',
        image='i3.jpg',
        question='Can your design protect the users from danger?',
        description='Preliminary action allows reflective material to respond to direct light; the patterns redirect the light back, making wearer more visible at night. Lost Value designed a reflective scarf that is produced for the urban cyclists or runners.')
    Post.objects.create(
        id=44,
        catalog='Interaction',
        catagory='Reactive Fashion',
        image='i4.jpg',
        question='Can your design automatically respond to user behaviour and outside environmental conditions such as light, movement, touch etc.?',
        description='Reactive fashion gives the impression that the clothing is alive, opening itself to breathe and take in the rays of light. Fashion designer and Professor Ying Gao is exploring the concept of transformative & interactive fashion collections with the environment such as light, movement, wind or touch using interactive microelectronic technology.')
    Post.objects.create(
        id=45,
        catalog='Interaction',
        catagory='Fairytale Fashion',
        image='i5.jpg',
        question='Can your design provoke curiosity and mutual discovery through various interactions with clothing or your design system?',
        description='The magical element in design can help to potentially deliver a series of future discoveries and the life of an object is dramatically increased as users remain captivated in anticipation of the next event (Chapman, 2005). Fairytale Fashion is created by Diana Eng. They are producing a collection of magical clothing incorporating science and technology like inflatable, deployable structures, muscle wire and microcontrollers.')
    Post.objects.create(
        id=46,
        catalog='Interaction',
        catagory='Tailoring',
        image='i6.jpg',
        question='Can your design will be fit for all body types?',
        description='Jasmin Schaitl is an artist and a fashion designer who designed Body-Index-Cloth through exploring the idea of the relationship between body and cloth. She suggested a new pattern making technique which is a visually and logically understandable system. She created a garment using the calculated parabolic formula which gave a standard index from which all body types could be tailored')
    Post.objects.create(
        id=47,
        catalog='Interaction',
        catagory='Notification',
        image='i7.PNG',
        question='Can you notify the consumer about your design regularly?',
        description='Just-in-time notifications and simulation of actionable information could support in motivating people to adapt their action point. For example, Web 3.0 RFID is possible to track products in real-time and enable actions like logistics companies being able to sell off spare space on long-haul shipping through auctions (Forum for the Future and Levi Strauss & Co, 2010)')
    Post.objects.create(
        id=48,
        catalog='Interaction',
        catagory='Feed forward',
        image='i8.PNG',
        question='Can you give the user a preview of future scenarios or demonstrate the results of their different actions or choices?',
        description='Reviewing the energy feed forward of ‘unsustainable’ products provides an opportunity to influence the users to make the right decision. STATIC! Suggested various designs which increase user awareness of how energy is used and for stimulating changes in energy behaviour. Heat is a form of energy that is often taken for granted. They designed disappearing pattern tiles using a thermo-chromic ink that reacts to heat, fading away to reflect splashes and intensities of hot-water use.')
    Post.objects.create(
        id=49,
        catalog='Interaction',
        catagory='Etiquette Views',
        image='i9.PNG',
        question='How can you design to motivate users behavioural change through playful experiences?',
        description='The use of positive feedback can enhance the social connectedness. Takkiainen is a jacket for lonely or bored people who want to interact with other people. The Jacket helps the wearer to get in contact with others. The materials used are Velcro strips of different widths. When these materials touch each other, they grab onto each other. The lonely user can be happily connected with others .')
    Post.objects.create(
        id=50,
        catalog='Interaction',
        catagory='Milieu response',
        image='i10.PNG',
        question='Can your design communicate with people to encourage them to practice and follow environmental rules?',
        description='Suzanne Goodwin designed clothing collections that respond to rapidly changing weather patterns. She emphasised the growing concerns of climate change through fashion design. The garments are responsive to the elements of sun, wind and rain. Patterns appear and disappear depending on weather conditions. The collection of fashion products offers to increase awareness of environmental issues and also possesses a pleasure element')
    Post.objects.create(
        id=51,
        catalog='Social Conversation',
        catagory='Symbiotic Bond',
        image='s1.jpg',
        question='Can your design promote positive symbiotic relationships?',
        description='Fashion 4 Development (F4D) is a global platform that implements creative fashion design strategies for sustainable economic growth through engagement with multi-stakeholder partnerships. It aims to improve society and the planet, especially in developing nations supported by UNESCO.')
    Post.objects.create(
        id=52,
        catalog='Social Conversation',
        catagory='Impetus Actors',
        image='s2.jpg',
        question='How can local actors, possible users and other stakeholders contribute to sustainability in fashion design development?',
        description='Collaborative design processes could potentially foster a more connected and active engagement with fashion and textiles. One of the most extensive craft micro-production networks is Ponoko which brings together creators, material suppliers, digital fabricators, DIYers & buyers in a collaborative design environment.')
    Post.objects.create(
        id=53,
        catalog='Social Conversation',
        catagory='Enabling Solution',
        image='s3.jpg',
        question='How can your project support local creative communities to enable solutions for supporting sustainable fashion?',
        description='Enabling Solutions are systems of products, services and organisational tools that enable individuals or communities to achieve a result using at best their skills and abilities (Manzini, 2004). ‘Instructables’ is an active DIY community where any individual can share their design projects and network with others regarding everyday life objects, abilities and skills.')
    Post.objects.create(
        id=54,
        catalog='Social Conversation',
        catagory='Localisation',
        image='s4.jpg',
        question='How can local products and production be worth giving up global sourcing and production?',
        description='One of the main issues of the unsustainable fashion and textile practices are linked to the scale of production and consumption and its use of resources. High volume production and consumption mean that we buy and discard more than ever (Fletcher, 2008). Dr Kate Fletcher deeply investigated various possibilities of the local design and wisdom. Her project captures the ‘local wisdom’, giving a platform to flourish and inspire.')
    Post.objects.create(
        id=55,
        catalog='Social Conversation',
        catagory='Clique Learning',
        image='s5.PNG',
        question='Can your project support to frame environmental issues in the context of everyday life clothing use as community learning service?',
        description='When we are actively engaged in, learning about or teaching something, we tend to feel more fulfilled. Amy Smallwood promotes a creative business for young children aged 5-9 years through encouraging to learn about fashion and design with a creative mind. Working with young people in a meaningful and educational way Amy captured the vibrancy and enjoyment of children’s creativity throughout the workshop using recycled materials')
    Post.objects.create(
        id=56,
        catalog='Social Conversation',
        catagory='Profilic Venture',
        image='s6.jpg',
        question='How will your service or product be of benefit to society for creating a creative enterprise?',
        description='Local action can help to develop human creativeness as we inventively respond to problems with the resources and expertise that are to hand. Local products inspire and challenge the community while at the same time, creating jobs and making use of local resources. Funding platforms for creative projects to artists or designers.')
    Post.objects.create(
        id=57,
        catalog='Social Conversation',
        catagory='Power Shift',
        image='s7.jpg',
        question='How can your project lead to new forms of cultural exchange and enhance positive human values?',
        description='In order to achieve the social and environmental standards, promoting positive social and cultural improvement and consumer participation is significantly important to enhance quality of life. Von Busch has explored a method for questioning the forces at play between the global fashion system and small-scale local production using collaborative design practices. Equally, local scale projects such as the ‘community repair’ workshop provide spaces for skills development.')
    Post.objects.create(
        id=58,
        catalog='Social Conversation',
        catagory='Social Feedback',
        image='s8.jpg',
        question='How can your design system or service be catalysed by social learning?',
        description='People could be influenced consciously and subconsciously through social learning and in turn spread positive ideas to others in their social domain (Pettersen and Boks, 2008). Social feedback could encourage people that they are part of a collective movement that’s making a real difference e.g. Web 2.0, web-based communities and hosted services such as social-networking sites, wikis, video sharing site and blogs).')   
    Post.objects.create(
        id=59,
        catalog='Social Conversation',
        catagory='Social Service',
        image='s9.jepg',
        question='Can you design a service that will be an aid to small local design communities?',
        description='In order to maximize positive environmental and sociocultural conditions, social conversation is a crucial part to help achieve this level. Aid to Artisans provides a designer platform to a small community engaging with a third world culture. The background of their design strategies is to create value and innovation that can support beyond current capabilities engaging with diverse design communities and craftspeople.')
    Post.objects.create(
        id=60,
        catalog='Social Conversation',
        catagory='Way of Living',
        image='s10.jpg',
        question='How can you inspire people to lead greener, healthier and happy life through your design?',
        description='Re-structuring of sustainable life styles is central to sustainable development. Manzini, E. and Jégou, F. (2003) suggested the ‘Sustainable everyday’ which is a network of local and connected services and systems, drawing together a whole series of living strategies. Their website offers sustainable alternatives for urban living from ten different countries')
    return render(request,'blog/index.html')
def card(request):
    return render(request,'blog/index.html')
def choice(request):
    choice = Post.objects.filter(catalog='choice')
    choices = {
        'choice':choice[:5:],
        'choice1':choice[5::],
    }
    print(choices)
    return render(request,'blog/choice.html',choices)
def selection(request):
    print("hi")
    return None
def optimisation(request):
    choice = Post.objects.filter(catalog='Optimisation')
    choices = {
        'choice':choice[:5:],
        'choice1':choice[5::],
    }
    print(choice)
    return render(request,'blog/optimization.html',choices)
def empowerment(request):
    choice = Post.objects.filter(catalog='Empowerment')
    choices = {
        'choice':choice[:5:],
        'choice1':choice[5::],
    }
    print(choices)
    return render(request,'blog/empowerment.html',choices)
def interaction(request):
    choice = Post.objects.filter(catalog='Interaction')
    choices = {
        'choice':choice[:5:],
        'choice1':choice[5::],
    }
    print(choices)
    return render(request,'blog/interaction.html',choices)
def persuasion(request):
    choice = Post.objects.filter(catalog='persuasion')
    choices = {
        'choice':choice[:5:],
        'choice1':choice[5::],
    }
    print(choices)
    return render(request,'blog/persuasion.html',choices)
def social_conversation(request):
    choice = Post.objects.filter(catalog='Social Conversation')
    choices = {
        'choice':choice[:5:],
        'choice1':choice[5::],
    }
    print(choices)
    return render(request,'blog/socialconversation.html',choices)

