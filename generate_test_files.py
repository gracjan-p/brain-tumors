for step in range(4):
    for i, mat in enumerate(matrices[:4]):
        with h5py.File(f"{mat_path}\\{mat}", 'r') as file:
            image = file['cjdata']['image']
            label = int(file['cjdata']['label'][0])

            image = np.array(image)

            # normalize img values where [min, max] = [0, 1] and multiply to [0, 255]
            image = np.array(image) / np.max(image)
            image *= 255

            # 1 exposure, contrast
            if step == 1:
                image = exposure.equalize_hist(image)
                image = (image - (image.min())) / (image.max() - (image.min()))
                image *= 255

            # 2 add contrast stretching
            if step == 2:
                image[image <= 30] = 0
                image = exposure.equalize_hist(image)
                image = (image - (image.min())) / (image.max() - (image.min()))
                image *= 255

            # 3 clean background
            if step == 3:
                image[image <= 30] = 0

                image //= 100
                image *= 100

                image = exposure.equalize_hist(image)
                image = (image - (image.min())) / (image.max() - (image.min()))
                image *= 255

                # divide array and then multiply it by same number [50, 70, 120] // 100, * 100 => [0, 0, 100]


            image = np.array(image).astype(np.uint8)
            img_values = Image.fromarray(image)

            file_name = label_names[label] + f"_{i}_{step}.png"
            img_values.save(data_path + '\\test\\' + file_name)