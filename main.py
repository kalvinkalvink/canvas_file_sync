from pathlib import Path

from canvasapi import Canvas
from canvasapi import folder

from canvas_grab import utils
from canvas_grab.config import directoryConfig, canvasApiConfig, feature

if __name__ == '__main__':
    canvas = Canvas(canvasApiConfig.API_URL, canvasApiConfig.API_KEY)
    for course_id, course_name in canvasApiConfig.MY_COURSE_LIST.items():
        # each course
        course = canvas.get_course(course_id)
        course_directory = Path(directoryConfig.BASE_DIRECTORY, course_name)
        print(course)

        # assignments = course.get_assignments()
        # for assignment in assignments:
        #     print(assignment.__dict__)
        # break

        if feature.FILES:
            print("downloading files")
            folders = course.get_folders()
            for folder in folders:  # type: folder.Folder
                # eacher folder in course
                folder_directory = Path(course_directory, folder.full_name)
                utils.File.make_dir(folder_directory)
                files = folder.get_files()
                for file in files:  # type: file.File
                    # each files in folder
                    print(file)
                    utils.Request.download_files(folder_directory=folder_directory, file=file)
